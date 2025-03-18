// filepath: lib/main.dart
// ignore_for_file: use_key_in_widget_constructors, library_private_types_in_public_api

import 'package:flutter/material.dart';
import 'package:excel/excel.dart';
import 'dart:io';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'EEG Results Visualizer',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: ResultsPage(),
    );
  }
}

class ResultsPage extends StatefulWidget {
  @override
  _ResultsPageState createState() => _ResultsPageState();
}

class _ResultsPageState extends State<ResultsPage> {
  List<List<dynamic>> rows = [];

  @override
  void initState() {
    super.initState();
    _readExcelFile();
  }

  void _readExcelFile() async {
    var file = 'autogluon_results.xlsx';
    var bytes = File(file).readAsBytesSync();
    var excel = Excel.decodeBytes(bytes);

    for (var table in excel.tables.keys) {
      rows = excel.tables[table]!.rows;
    }

    setState(() {});
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('EEG Results Visualizer'),
      ),
      body: rows.isEmpty
          ? Center(child: CircularProgressIndicator())
          : SingleChildScrollView(
              scrollDirection: Axis.horizontal,
              child: DataTable(
                columns: rows[0]
                    .map((header) => DataColumn(label: Text(header.toString())))
                    .toList(),
                rows: rows
                    .sublist(1)
                    .map((row) => DataRow(
                          cells: row
                              .map((cell) => DataCell(Text(cell.toString())))
                              .toList(),
                        ))
                    .toList(),
              ),
            ),
    );
  }
}