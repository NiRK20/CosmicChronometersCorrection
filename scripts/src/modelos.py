c = 299792.458#km/s

def free_par(theta, corr, flat):
    if flat:
        if corr:
            h0, wm, f = theta
            return h0, wm, 1-wm, f
        else:
            h0, wm = theta
            return h0, wm, 1-wm, 1
    else:
        if corr:
            h0, wm, wl, f = theta
            return h0, wm, wl, f
        else:
            h0, wm, wl = theta
            return h0, wm, wl, 1

MODELOS = {
    "Plano_1": {
        "model": "Plano_1",
        "Corr": False,
        "Flat": True,
        "params":{
            "h0": {"prior": {"min": 40.0, "max": 100.0}, "latex": r"H_{0}"},
            "wm": {"prior": {"min": 0.0, "max": 3.0}, "latex": r"\Omega_{m}"},
            "wl": {"derived": "lambda wm: 1 - wm"}
        },
        "values": {
            "h0": 69.1929957609451,
            "wm": 0.2480895086492853
        },
        "index": {"h0": 0, "wm": 1},
        "label": r"$\Lambda$CDM plano sem f"
    },
    "Plano_f": {
        "model": "Plano_f",
        "Corr": True,
        "Flat": True,
        "params":{
            "h0": {"prior": {"min": 40.0, "max": 100.0}, "latex": r"H_{0}"},
            "wm": {"prior": {"min": 0.0, "max": 3.0}, "latex": r"\Omega_{m}"},
            "wl": {"derived": "lambda wm: 1 - wm"},
            "f": {"prior":{"min": 0.1, "max": 2.0}, "latex": "f"}
        },
        "values": {
            "h0": 69.1929957609451,
            "wm": 0.2480895086492853,
            "f": 0.9
        },
        "index": {"h0": 0, "wm": 1, "f": 3},
        "label": r"$\Lambda$CDM plano com f"
    },
    "Curvo_1": {
        "model": "Curvo_1",
        "Corr": False,
        "Flat": False,
        "params":{
            "h0": {"prior": {"min": 40.0, "max": 100.0}, "latex": r"H_{0}"},
            "wm": {"prior": {"min": 0.0, "max": 3.0}, "latex": r"\Omega_{m}"},
            "wl": {"prior": {"min": -3.0, "max": 3.0}, "latex": r"\Omega_{\Lambda}"},
            "wk": {"derived": "lambda wm, wl: 1 - wm - wl"}
        },
        "values": {
            "h0": 69.1929957609451,
            "wm": 0.2480895086492853,
            "wl": 0.6862431649000225
        },
        "index": {"h0": 0, "wm": 1, "wl": 2, "wk": 3},
        "label": r"$\Lambda$CDM curvo sem f"
    },
    "Curvo_f": {
        "model": "Curvo_f",
        "Corr": True,
        "Flat": False,
        "params":{
            "h0": {"prior": {"min": 40.0, "max": 100.0}, "latex": r"H_{0}"},
            "wm": {"prior": {"min": 0.0, "max": 3.0}, "latex": r"\Omega_{m}"},
            "wl": {"prior": {"min": -3.0, "max": 3.0}, "latex": r"\Omega_{\Lambda}"},
            "wk": {"derived": "lambda wm, wl: 1 - wm - wl"},
            "f": {"prior": {"min": 0.1, "max":2.0}, "latex": "f"},
        },
        "values": {
            "h0": 69.1929957609451,
            "wm": 0.2480895086492853,
            "wl": 0.6862431649000225,
            "f": 0.9
        },
        "index": {"h0": 0, "wm": 1, "wl": 2, "wk": 3, "f": 4},
        "label": r"$\Lambda$CDM curvo com f"
    },
}
