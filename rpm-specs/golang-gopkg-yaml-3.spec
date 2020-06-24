# Generated by go2rpm
%bcond_without check

# https://github.com/go-yaml/yaml
%global goipath         gopkg.in/yaml.v3
%global forgeurl        https://github.com/go-yaml/yaml
%global commit          cdc409dda467df8d60dc5c7d18f38e810979de95

%gometa

%global goaltipaths     gopkg.in/v3/yaml

%global common_description %{expand:
The yaml package enables Go programs to comfortably encode and decode YAML
values. It was developed within Canonical as part of the juju project, and is
based on a pure Go port of the well-known libyaml C library to parse and
generate YAML data quickly and reliably.

The yaml package supports most of YAML 1.2, but preserves some behavior from 1.1
for backwards compatibility.

Specifically, as of v3 of the yaml package:

 - YAML 1.1 bools (yes/no, on/off) are supported as long as they are being
   decoded into a typed bool value. Otherwise they behave as a string. Booleans
   in YAML 1.2 are true/false only.
 - Octals encode and decode as 0777 per YAML 1.1, rather than 0o777 as specified
   in YAML 1.2, because most parsers still use the old format. Octals in the
   0o777 format are supported though, so new files work.
 - Does not support base-60 floats. These are gone from YAML 1.2, and were
   actually never supported by this package as it's clearly a poor choice.

and offers backwards compatibility with YAML 1.1 in some cases. 1.2, including
support for anchors, tags, map merging, etc. Multi-document unmarshalling is not
yet implemented, and base-60 floats from YAML 1.1 are purposefully not supported
since they're a poor design and are gone in YAML 1.2.}

%global golicenses      LICENSE NOTICE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Yaml support for the Go language

# Upstream license specification: Apache-2.0 and MIT
License:        ASL 2.0 and MIT
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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 21 07:44:40 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190622gitcdc409d
- Initial package
