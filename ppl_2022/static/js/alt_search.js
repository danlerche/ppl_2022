if (performance.navigation.type == 0 || performance.navigation.type == 1 || performance.navigation.type == 2) {
document.getElementById("searchType").selectedIndex = 'Keyword';
}

document.getElementById('altSearch').searchType.onchange = function() {
if (document.getElementById("searchType").value == "Keyword") {
var newaction = "https://search.pentictonlibrary.ca/Union/Search";
document.getElementById('altSearch').action = newaction;
var name = "lookfor";
document.getElementById('altSearchInput').name = name;
var placeholder = "Search the catalogue by keyword";
document.getElementById('altSearchInput').placeholder = placeholder;
}

else if (document.getElementById("searchType").value == "Title") {
var newaction = "https://search.pentictonlibrary.ca/Union/Search";
document.getElementById('altSearch').action = newaction;
var name = "lookfor";
document.getElementById('altSearchInput').name = name;
var placeholder = "Search the catalogue by title";
document.getElementById('altSearchInput').placeholder = placeholder;
}

else if (document.getElementById("searchType").value == "StartOfTitle") {
var newaction = "https://search.pentictonlibrary.ca/Union/Search";
document.getElementById('altSearch').action = newaction;
var name = "lookfor";
document.getElementById('altSearchInput').name = name;
var placeholder = "Search the catalogue by the start of the title";
document.getElementById('altSearchInput').placeholder = placeholder;
}

else if (document.getElementById("searchType").value == "Series") {
var newaction = "https://search.pentictonlibrary.ca/Union/Search";
document.getElementById('altSearch').action = newaction;
var name = "lookfor";
document.getElementById('altSearchInput').name = name;
var placeholder = "Search the catalogue by series";
document.getElementById('altSearchInput').placeholder = placeholder;
}

else if (document.getElementById("searchType").value == "Author") {
var newaction = "https://search.pentictonlibrary.ca/Union/Search";
document.getElementById('altSearch').action = newaction;
var name = "lookfor";
document.getElementById('altSearchInput').name = name;
var placeholder = "Search the catalogue by author";
document.getElementById('altSearchInput').placeholder = placeholder;
}

else if (document.getElementById("searchType").value == "Subject") {
var newaction = "https://search.pentictonlibrary.ca/Union/Search";
document.getElementById('altSearch').action = newaction;
var name = "lookfor";
document.getElementById('altSearchInput').name = name;
var placeholder = "Search the catalogue by subject";
document.getElementById('altSearchInput').placeholder = placeholder;
}

else if (document.getElementById("searchType").value == "website") {
var newaction = "/search";
document.getElementById('altSearch').action = newaction;
var newname = "query";
document.getElementById('altSearchInput').name = newname;
var newplaceholder = "Search all other library content";
document.getElementById('altSearchInput').placeholder = newplaceholder;
}
};

function radioSearch() {
	if (document.getElementById('searchCatalogue').checked) {
        document.getElementById('altSearch').style.display = 'block';
        document.getElementById('websiteSearch').style.display = 'none';
    }

    else if (document.getElementById('searchWebsite').checked) {
        document.getElementById('websiteSearch').style.display = 'block';
        document.getElementById('altSearch').style.display = 'none';
    }
}
