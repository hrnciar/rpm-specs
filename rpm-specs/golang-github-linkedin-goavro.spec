# Generated by go2rpm
# https://github.com/linkedin/goavro/issues/214
%ifnarch %{arm} %{ix86}
%bcond_without check
%endif

# https://github.com/linkedin/goavro
%global goipath         github.com/linkedin/goavro
Version:                2.9.8

%gometa

%global common_description %{expand:
Goavro is a library that encodes and decodes Avro data.}

%global golicenses      LICENSE
%global godocs          examples AUTHORS README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Library that encodes and decodes Avro data

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/golang/snappy)

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
* Tue Jul 28 22:55:07 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.9.8-1
- Update to 2.9.8

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 22:54:34 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.8.4-1
- Initial package
