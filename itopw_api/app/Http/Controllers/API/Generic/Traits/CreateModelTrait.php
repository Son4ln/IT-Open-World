<?php

namespace App\Http\Controllers\API\Generic\Traits;

use Illuminate\Http\Request;

trait CreateModelTrait
{
    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store()
    {
        // $data = slug_convert($this->request->all());
        $serie = $this->get_model_class()::create($this->request->all());
        return response()->json(
            [
                "data" => $serie,
                "message" => __('messages.created')
            ], 200);
    }
}
