# Generated by go2rpm
%bcond_without check

# https://github.com/alecthomas/units
%global goipath         github.com/alecthomas/units
%global commit          f65c72e2690dc4b403c8bd637baf4611cd4c069b

%gometa

%global common_description %{expand:
Helpful unit multipliers and functions for go.}

%global golicenses      COPYING
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.10%{?dist}
Summary:        Helpful unit multipliers and functions for go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
%endif

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
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 20:49:24 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.8.20200126gitf65c72e
- Bump to commit f65c72e2690dc4b403c8bd637baf4611cd4c069b

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 20 23:24:02 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.6.20181111git2efee85
- Update to new macros

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git2efee85
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 11 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20181111git2efee85
- Update to new Go packaging

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git2efee85
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git2efee85
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 11 2017 mosquito <sensor.wen@gmail.com> - 0-0.1.git2efee85
- Initial package

