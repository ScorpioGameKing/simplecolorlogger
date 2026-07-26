{
  description = "A very basic flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = { self, nixpkgs }: 

    let
      pkgs = import nixpkgs  {
        system = "x86_64-linux";
      };
    in

    {

    devShells.x86_64-linux.default = pkgs.mkShell {
      packages = [
        (pkgs.python3.withPackages (python-pkgs: [
          python-pkgs.pip
          python-pkgs.colorama
          python-pkgs.setuptools
          python-pkgs.wheel
          python-pkgs.twine
        ]))
      ];
      shellHook = ''
          echo Python Development Flake Enabled
        '';
    };
  };
}
