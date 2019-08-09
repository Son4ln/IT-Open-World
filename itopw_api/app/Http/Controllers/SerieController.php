<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Series;

class SerieController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        return Series::all();
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        $data = slug_convert($request->all());
        $serie = Series::create($data);
        return response()->json(
            [
                "data" => $serie,
                "message" => __('messages.created')
            ], 200);
    }

    /**
     * Display the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function show(Series $serie)
    {
        return $serie;
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function edit($id)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, Series $serie)
    {
        $data = slug_convert($request->all());
        $serie->update($data);

        return response()->json(
            [
                "data" => $serie,
                "message" => __('messages.updated')
            ], 200);
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function destroy(Series $serie)
    {
        $serie->delete();

        return response()->json($serie, 'Xóa dữ liệu thành công!');
    }

    public function slug_convert($data)
    {
        $data['slug'] = \Illuminate\Support\Str::slug($data['name'], '-');
        return $data;
    }
}
