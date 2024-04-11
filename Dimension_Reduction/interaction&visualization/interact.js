let highlightedIndex = null;

function highlightPoints(index) {
    if (highlightedIndex === index) {
        // If the clicked circle is already highlighted, unhighlight all circles
        d3.selectAll("circle").style("opacity", 1).attr("r", 5);
        highlightedIndex = null;
    } else {
        // Otherwise, highlight the clicked circle and unhighlight all other circles
        d3.selectAll("circle").style("opacity", 0.1);
        d3.selectAll("circle[data-index='" + index + "']")
        .style("opacity", 1)
        .attr("r", 10); // Increase radius
        highlightedIndex = index;
    }
}

async function fetchdata1() {
    try {
        var PCA_data = await d3.csv('./pca_data_cluster.csv');

        PCA_data.forEach(row => {
            row.index = +row.index;
            row.PC1 = +row.PC1;
            row.PC2 = +row.PC2;
            row.Cluster = +row.Cluster;
        });

        const colorScale = d3.scaleSequential(d3.interpolateRdBu)
            .domain([-0.75, 1.25]);

        const margin = { top: 20, right: 30, bottom: 60, left: 50 },
            width = 460 - margin.left - margin.right,
            height = 460 - margin.top - margin.bottom;

        const svg = d3.select("#scatter-diagram1")
            .append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        const x = d3.scaleLinear()
            .domain([0, 1])
            .range([0, width]);

        svg.append("g")
            .attr("transform", "translate(0," + (height + 10) + ")")
            .call(d3.axisBottom(x));

        const y = d3.scaleLinear()
            .domain([0, 1])
            .range([height, 0]);

        svg.append("g")
            .attr("transform", "translate(-10,0)")
            .call(d3.axisLeft(y));

        svg.append('g')
            .selectAll("dot")
            .data(PCA_data)
            .enter()
            .append("circle")
            .attr("cx", function (d) { return x(d.PC1); })
            .attr("cy", function (d) { return y(d.PC2); })
            .attr("r", 5)
            .style("fill", d => colorScale(d.Cluster))
            .attr("transform", "translate(2.5, -2.5)")
            .attr("data-index", function (d) { return d.index; }) // Add data-index attribute
            .on("click", function (d) { // Add click event listener
                highlightPoints(d.index);
            });

        svg.append("text")
            .attr("x", width / 2)
            .attr("y", height + margin.bottom - 5)
            .style("text-anchor", "middle")
            .text("PCA Scatter Diagram");
    } catch (error) {
        console.error("An error occurred:", error);
    }
}
fetchdata1();

async function fetchdata2() {
    // Similar to fetchdata1, but for "#scatter-diagram2" and './TSNE.csv'
    try {
        var TSNE_data = await d3.csv('./tsne_data_cluster.csv');

        TSNE_data.forEach(row => {
            row.index = +row.index;
            row.TSNE1 = +row.TSNE1;
            row.TSNE2 = +row.TSNE2;
            row.Cluster = +row.Cluster;
        });

        const colorScale = d3.scaleSequential(d3.interpolateRdBu)
            .domain([-0.75, 1.25]);

        const margin = { top: 20, right: 30, bottom: 60, left: 50 },
            width = 460 - margin.left - margin.right,
            height = 460 - margin.top - margin.bottom;

        const svg = d3.select("#scatter-diagram2")
            .append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        const x = d3.scaleLinear()
            .domain([0, 1])
            .range([0, width]);

        svg.append("g")
            .attr("transform", "translate(0," + (height + 10) + ")")
            .call(d3.axisBottom(x));

        const y = d3.scaleLinear()
            .domain([0, 1])
            .range([height, 0]);

        svg.append("g")
            .attr("transform", "translate(-10,0)")
            .call(d3.axisLeft(y));

        svg.append('g')
            .selectAll("dot")
            .data(TSNE_data)
            .enter()
            .append("circle")
            .attr("cx", function (d) { return x(d.TSNE1); })
            .attr("cy", function (d) { return y(d.TSNE2); })
            .attr("r", 5)
            .style("fill", d => colorScale(d.Cluster))
            .attr("transform", "translate(2.5, -2.5)")
            .attr("data-index", function (d) { return d.index; }) // Add data-index attribute
            .on("click", function (d) { // Add click event listener
                highlightPoints(d.index);
            });

        svg.append("text")
            .attr("x", width / 2)
            .attr("y", height + margin.bottom - 5)
            .style("text-anchor", "middle")
            .text("TSNE Scatter Diagram");
    }
    catch (error) {
        console.error("An error occurred:", error);
    }
}
fetchdata2();

async function fetchdata3() {
    // Similar to fetchdata1, but for "#scatter-diagram3" and './MDS.csv'
    try {
        var MDS_data = await d3.csv('./mds_data_cluster.csv');

        MDS_data.forEach(row => {
            row.index = +row.index;
            row.MDS1 = +row.MDS1;
            row.MDS2 = +row.MDS2;
            row.Cluster = +row.Cluster;
        });

        const colorScale = d3.scaleSequential(d3.interpolateRdBu)
            .domain([-0.75, 1.25]);

        const margin = { top: 20, right: 30, bottom: 60, left: 50 },
            width = 460 - margin.left - margin.right,
            height = 460 - margin.top - margin.bottom;

        const svg = d3.select("#scatter-diagram3")
            .append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        const x = d3.scaleLinear()
            .domain([0, 1])
            .range([0, width]);

        svg.append("g")
            .attr("transform", "translate(0," + (height + 10) + ")")
            .call(d3.axisBottom(x));

        const y = d3.scaleLinear()
            .domain([0, 1])
            .range([height, 0]);

        svg.append("g")
            .attr("transform", "translate(-10,0)")
            .call(d3.axisLeft(y));

        svg.append('g')
            .selectAll("dot")
            .data(MDS_data)
            .enter()
            .append("circle")
            .attr("cx", function (d) { return x(d.MDS1); })
            .attr("cy", function (d) { return y(d.MDS2); })
            .attr("r", 5)
            .style("fill", d => colorScale(d.Cluster))
            .attr("transform", "translate(2.5, -2.5)")
            .attr("data-index", function (d) { return d.index; }) // Add data-index attribute
            .on("click", function (d) { // Add click event listener
                highlightPoints(d.index);
            });

        svg.append("text")
            .attr("x", width / 2)
            .attr("y", height + margin.bottom - 5)
            .style("text-anchor", "middle")
            .text("MDS Scatter Diagram");
    }
    catch (error) {
        console.error("An error occurred:", error);
    }
}
fetchdata3();

async function fetchdata4() {
    try {
        var UMAP_data = await d3.csv('./umap_data_cluster.csv');

        UMAP_data.forEach(row => {
            row.index = +row.index;
            row.UMAP1 = +row.UMAP1;
            row.UMAP2 = +row.UMAP2;
            row.Cluster = +row.Cluster;
        });

        const colorScale = d3.scaleSequential(d3.interpolateRdBu)
            .domain([-0.75, 1.25]);

        const margin = { top: 20, right: 30, bottom: 60, left: 50 },
            width = 460 - margin.left - margin.right,
            height = 460 - margin.top - margin.bottom;

        const svg = d3.select("#scatter-diagram4")
            .append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        const x = d3.scaleLinear()
            .domain([0, 1])
            .range([0, width]);

        svg.append("g")
            .attr("transform", "translate(0," + (height + 10) + ")")
            .call(d3.axisBottom(x));

        const y = d3.scaleLinear()
            .domain([0, 1])
            .range([height, 0]);

        svg.append("g")
            .attr("transform", "translate(-10,0)")
            .call(d3.axisLeft(y));

        svg.append('g')
            .selectAll("dot")
            .data(UMAP_data)
            .enter()
            .append("circle")
            .attr("cx", function (d) { return x(d.UMAP1); })
            .attr("cy", function (d) { return y(d.UMAP2); })
            .attr("r", 5)
            .style("fill", d => colorScale(d.Cluster))
            .attr("transform", "translate(2.5, -2.5)")
            .attr("data-index", function (d) { return d.index; }) // Add data-index attribute
            .on("click", function (d) { // Add click event listener
                highlightPoints(d.index);
            });

        svg.append("text")
            .attr("x", width / 2)
            .attr("y", height + margin.bottom - 5)
            .style("text-anchor", "middle")
            .text("UMAP Scatter Diagram");
    }
    catch (error) {
        console.error("An error occurred:", error);
    }
}
fetchdata4();