# Generated by go2rpm
%bcond_without check

# https://github.com/go-yaml/yaml
%global goipath         gopkg.in/yaml.v1
%global forgeurl        https://github.com/go-yaml/yaml
%global commit          9f9df34309c04878acc86042b16630b0f696e1de

%gometa

# Remove in F33:
%global godevelheader %{expand:
Obsoletes:      golang-gopkg-yaml-devel < 1-28
}

%global goaltipaths     gopkg.in/v1/yaml

%global common_description %{expand:
The yaml package enables Go programs to comfortably encode and decode YAML
values. It was developed within Canonical as part of the juju project, and is
based on a pure Go port of the well-known libyaml C library to parse and
generate YAML data quickly and reliably.

The yaml package supports most of YAML 1.1 and 1.2, including support for
anchors, tags, map merging, etc. Multi-document unmarshalling is not yet
implemented, and base-60 floats from YAML 1.1 are purposefully not supported
since they're a poor design and are gone in YAML 1.2.}

%global golicenses      LICENSE LICENSE.libyaml
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.4%{?dist}
Summary:        Yaml support for the Go language

License:        MIT and LGPLv3
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.2.20190622git9f9df34
- Add Obsoletes for old name

* Sun Apr 21 07:41:21 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190622git9f9df34
- Initial package