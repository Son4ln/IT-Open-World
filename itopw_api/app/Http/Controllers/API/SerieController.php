<?php

namespace App\Http\Controllers\API;

use Illuminate\Http\Request;
use App\Http\Controllers\API\Generic\APIController;

class SerieController extends APIController
{
    use \App\Http\Controllers\API\Generic\Traits\ListModelTrait;
    use \App\Http\Controllers\API\Generic\Traits\CreateModelTrait;
    protected $model = "App\Series";
}
