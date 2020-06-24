# Generated by go2rpm
%bcond_without check

# https://github.com/Nvveen/Gotty
%global goipath         github.com/Nvveen/Gotty
%global commit          cd527374f1e5bff4938207604a14f2e38a9cf512

%gometa

%global common_description %{expand:
Gotty is a library written in Go that provides interpretation and loading of
Termcap database files.}

%global golicenses      LICENSE
%global godocs          README TODO

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Interpretation and loading of Termcap database files

License:        BSD
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

* Thu Jul 04 19:38:15 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20190705gitcd52737
- Initial package