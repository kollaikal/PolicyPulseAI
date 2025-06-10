# spark_model.py
from pyspark.sql import SparkSession
from pyspark.ml.feature import HashingTF, IDF, Tokenizer
from pyspark.ml.classification import LogisticRegression
from pyspark.ml import Pipeline

def predict_passage_probability(bills):
    spark = SparkSession.builder.appName("PolicyPassagePrediction").getOrCreate()

    rows = [
        {"text": b["summary"], "label": int(b.get("status", "Pending") == "Passed")}
        for b in bills if b.get("summary") and b.get("status")
    ]

    # Handle empty dataset
    if not rows:
        return "N/A"

    df = spark.createDataFrame(rows)

    # Same pipeline
    tokenizer = Tokenizer(inputCol="text", outputCol="words")
    hashingTF = HashingTF(inputCol="words", outputCol="rawFeatures", numFeatures=1000)
    idf = IDF(inputCol="rawFeatures", outputCol="features")
    lr = LogisticRegression(maxIter=10, regParam=0.01)
    pipeline = Pipeline(stages=[tokenizer, hashingTF, idf, lr])

    model = pipeline.fit(df)

    # Predict on latest bill with summary
    latest = next((b for b in reversed(bills) if b.get("summary")), None)
    if not latest:
        return "N/A"

    latest_df = spark.createDataFrame([{"text": latest["summary"]}])
    prediction = model.transform(latest_df).collect()[0]
    prob = float(prediction["probability"][1]) * 100
    return f"{prob:.2f}%"
