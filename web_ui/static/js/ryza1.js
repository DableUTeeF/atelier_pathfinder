class Graph{
    constructor(size){
        this.size = size;
        this.adj_matrix = Array.from({length: size}, e => Array(size).fill(0));;
        this.vertex_data = Array(size).fill('');
    }

    add_edge(u, v, w){
        if ((0 <= u < this.size) && (0 <= v < this.size)){
            this.adj_matrix[u][v] = w;
        }
    }

    add_vertex_data(vertex, data){
        if (0 <= vertex < this.size){
            this.vertex_data[vertex] = data;
        }
    }
}


function get_path(g, predecessors, start_vertex_data, end_vertex_data){
    var path = [];
    var current = g.vertex_data.indexOf(end_vertex_data);
    while (current != null){
        path.splice(0, 0, g.vertex_data[current]);
        current = predecessors[current];
        if (current == g.vertex_data.indexOf(start_vertex_data)){
            path.splice(0, 0, start_vertex_data);
            break
        }
    }
    return [path.join('->'), path]
}


function dijkstra(g, start_vertex_data, end_vertex_data){
    var start_vertex = g.vertex_data.indexOf(start_vertex_data);
    var end_vertex = g.vertex_data.indexOf(end_vertex_data);
    var distances = Array(g.size).fill(Infinity);
    var predecessors = Array(g.size).fill(null);
    distances[start_vertex] = 0;
    var visited = Array(g.size).fill(false);

    for (let dummy = 0; dummy < g.size; dummy++){
        let min_distance = Infinity;
        let u = null;
        for (let i = 0; i < g.size; i++){
            if ((!visited[i]) && (distances[i] < min_distance)){
                min_distance = distances[i];
                u = i;
            }
        }
        if (u === null){
            break;
        }
        visited[u] = true;
        for (let v = 0; v < g.size; v++){
            if (g.adj_matrix[u][v] != 0 && !visited[v]){
                let alt = distances[u] + g.adj_matrix[u][v];
                if (alt < distances[v]){
                    distances[v] = alt;
                    predecessors[v] = u;
                }
            }
        }
    }
    var [path, all_paths] = get_path(g, predecessors, start_vertex_data, end_vertex_data);
    return [distances, distances[end_vertex], path, all_paths];
}


function get_all_distances(g, src1, src2, src3, dst, all_path_distances){
    var [all_distances1, distance1, path1, all_paths1] = dijkstra(g, src1, dst);
    for (let i=1; i < all_paths1.length - 1; i++){
        var item = all_paths1[i];
        var [all_distances2, distance2, path2, all_paths2] = dijkstra(g, src2, item);
        if (src3 === null){
            all_path_distances[`${path1}\n${path2}`] = distance1 + distance2;
        }
        else{
            var [all_distances3, distance3, path3, all_paths3] = dijkstra(g, src3, item);
            all_path_distances[`${path1}\n${path2}\n${path3}`] = distance1 + distance2 + distance3;
            for (let j=1; j < all_paths2.length - 1; j++){
                let item2 = all_paths2[j];
                var [all_distances3, distance3, path3, all_paths3] = dijkstra(g, src3, item2);
                all_path_distances[`${path1}\n${path2}\n${path3}`] = distance1 + distance2 + distance3;            }
        }
    }
    var [all_distances2, distance2, path2, all_paths2] = dijkstra(g, src2, dst);
    path2 = all_paths2.splice(0, all_paths2.length-1).join('->')
    if (src3 === null){
        all_path_distances[`${path1}\n${path2}`] = distance1 + distance2 - 1;
    }
    else {
        var [all_distances3, distance3, path3, all_paths3] = dijkstra(g, src3, dst);
        path3 = all_paths3.splice(0, all_paths3.length-1).join('->')
        all_path_distances[`${path1}\n${path2}\n${path3}`] = distance1 + distance2 + distance3 - 2;
    }
    return all_path_distances;
}


var categories = {};
var item2idx = {};
var index = 0;

for (let [name, item] of Object.entries(ryza_data)) {
    item2idx[name] = index++;
    for (let cat of item['categories']){
        if (cat.startsWith('(')){
            if (!(cat in categories)){
                categories[cat] = {'items': []};
            }
            categories[cat]['items'].push(name);
        }
    }
}

var edges = [];
var names = [];
var id2name = {}

for (let [name, item] of Object.entries(ryza_data)){
    names.push(name);
    id2name[name.toLowerCase().replace(' ', '-').replace("'", "-")] = name;
    if ('ingredients' in item){
        for (let ing of item['ingredients']){
            if (ing.startsWith('(')){
                for (let cat of categories[ing]['items']){
                    edges.push([item2idx[cat], item2idx[name], 1.1]);
                }
            }
            else{
                edges.push([item2idx[ing], item2idx[name], item['cost']]);
            }
        }
    }
}

var g = new Graph(names.length)
for (var i = 0; i < names.length; i++){
    g.add_vertex_data(i, names[i]);
}
for (var i = 0; i < edges.length; i++){
    g.add_edge(edges[i][0], edges[i][1], edges[i][2]);
}

function run_test(){
    var srcs = ['Clean Water', 'Fertile Soil', 'Goldinite'];
    var dst = 'Brave Emblem';
    var all_path_distances = {};
    for (let src1 of srcs){
        for (let src2 of srcs){
            for (let src3 of srcs){
                if ((src1 != src2) && (src2 != src3) && (src1 != src3)){
                    all_path_distances = get_all_distances(g, src1, src2, src3, dst, all_path_distances);
                }
            }
        }
    }
    let min = Math.min.apply(null, Object.values(all_path_distances).filter(function(n) { return !isNaN(n); }));
    for (let [k, v] of Object.entries(all_path_distances)){
        if (!isNaN(v) && v == min){
            console.log(k);
            console.log(v);
            console.log();
        }
    }
    
    var srcs = ['Fertile Soil', 'Goldinite'];
    var dst = 'Brave Emblem';
    var all_path_distances = {};
    for (let src1 of srcs){
        for (let src2 of srcs){
            if ((src1 != src2)){
                all_path_distances = get_all_distances(g, src1, src2, null, dst, all_path_distances);
            }
        }
    }
    min = Math.min.apply(null, Object.values(all_path_distances).filter(function(n) { return !isNaN(n); }));
    for (let [k, v] of Object.entries(all_path_distances)){
        if (!isNaN(v) && v == min){
            console.log(k);
            console.log(v);
            console.log();
        }
    }    
}

function find_path(){
    var item1 = selectedTexts[0].value;
    var item2 = selectedTexts[1].value;
    var item3 = selectedTexts[2].value;
    var item4 = selectedTexts[3].value;
    var srcs = [id2name[item1], id2name[item2]];
    if (item3 != "None"){
        srcs.push(id2name[item3]);
    }
    var dst = id2name[item4];
    var all_path_distances = {};
    for (let src1 of srcs){
        for (let src2 of srcs){
            for (let src3 of srcs){
                if ((src1 != src2) && (src2 != src3) && (src1 != src3)){
                    all_path_distances = get_all_distances(g, src1, src2, src3, dst, all_path_distances);
                }
            }
        }
    }
    console.log(item1, item2, item3);
    let min = Math.min.apply(null, Object.values(all_path_distances).filter(function(n) { return !isNaN(n); }));
    var outputs = document.getElementById('outputs');
    outputs.innerHTML = '';
    for (let [k, v] of Object.entries(all_path_distances)){
        if (
            !isNaN(v)
            && v == min
            )
        {
            
            for (let ins of k.split('\n')){
                var chained_items = ins.split('->');
                var row = document.createElement('div');
                row.setAttribute('class', 'row flex-nowrap');

                for (let item of chained_items){
                    let filename = item.toLowerCase().replace(' ', '-').replace("'", "-");
                    var iconImgElement = document.createElement('img');
                    iconImgElement.setAttribute('src', `https://barrelwisdom.com/media/games/ryza2/items/${filename}.webp?v=1`);
                    iconImgElement.setAttribute('icon-value', item);
                    iconImgElement.setAttribute('width', 52);
                    iconImgElement.setAttribute('height', 52);  
                    // iconImgElement.setAttribute('class', 'card-img-top');  
                    var iconTextElement = document.createElement('p');
                    iconTextElement.innerHTML = `${item}`;

                    var column = document.createElement('div');
                    column.setAttribute('class', 'col');

                    var card = document.createElement('div');
                    card.setAttribute('class', 'card border-hover-primary hover-scale');
                    var card_body = document.createElement('div');
                    card_body.setAttribute('class', 'card-body');

                    card_body.appendChild(iconImgElement);
                    card_body.appendChild(iconTextElement);
                    card.appendChild(card_body);
                    column.appendChild(card);
                    row.appendChild(column);
                }
        
                outputs.appendChild(row);    
            }
            var iconTextElement = document.createElement('div');
            iconTextElement.innerHTML = `${v}`;
            outputs.appendChild(iconTextElement);    
        }
    }

}