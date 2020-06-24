# Generated by go2rpm 1
%bcond_without check

# https://github.com/hajimehoshi/go-mp3
%global goipath         github.com/hajimehoshi/go-mp3
Version:                0.2.1

%gometa

%global common_description %{expand:
An MP3 decoder in pure Go based on PDMP3.}

%global golicenses      LICENSE
%global godocs          example AUTHORS README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        MP3 decoder in pure Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0
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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 05 05:17:13 EEST 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.1-1
- Initial package
