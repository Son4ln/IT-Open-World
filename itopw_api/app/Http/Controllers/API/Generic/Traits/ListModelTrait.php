<?php

namespace App\Http\Controllers\API\Generic\Traits;

use Illuminate\Http\Request;

trait ListModelTrait
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        return response()->json(
        [
            "data" => $this->get_queryset(),
        ], 200);
    }
}
