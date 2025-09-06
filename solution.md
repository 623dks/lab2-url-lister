# Lab 2 - Convert WordCount to UrlCount Solution

## How It Works
URLCount is built on the base MapReduce framework from WordCount, but it has been modified to extract and count URLs from input text. Specifically, it searches for `href` tags using a Java regex pattern of the form `href=".*"`. The Mapper iterates through each line, extracts all matching links, and removes the `href=` prefix.  

The Reducer sums the occurrences of each URL and outputs only those that appear **more than 5 times**. To address the limitations of Java/Hadoop combiners, a separate Combiner class is used. This Combiner counts occurrences locally but **does not apply the ">5 occurrences" filter**, ensuring no URLs are incorrectly discarded before the final reduction.

---

## How to Run

1. Ensure your system has **Java** and **Hadoop** installed.
2. Prepare input files and HDFS structure:
make prepare
3. Compile the Java URLCount program:
make URLCount
4. Run the Hadoop job:
make runURL
# Or time make runURL to record execution time
5. If running on Google Cloud Dataproc:
   - SSH into the master node.
   - Create your HDFS user directory:
hdfs dfs -mkdir -p hdfs://CLUSTERNAME-m/user/USERNAME
   - Run the same Makefile commands from the master node.

## Results from Timed Runs

| Environment       | Time (real) | Time (user) | Time (sys) |
|------------------|------------|------------|------------|
| 2-node Cluster    | 0m32.025s  | 0m6.465s   | 0m0.356s   |
| 4-node Cluster    | 0m30.423s  | 0m7.529s   | 0m0.343s   |

**Observations:**  
- The local run is much faster than the cluster runs due to no overhead of distributing tasks across nodes.  
- Cluster execution time is similar for 2-node and 4-node setups. This is expected for small datasets, where the overhead of distributing executables and files dominates the performance gain from extra nodes.  
- With larger datasets, cluster performance would improve as multiple cores across nodes can be utilized more efficiently.


