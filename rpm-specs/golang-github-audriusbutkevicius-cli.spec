# Generated by go2rpm
%bcond_without check

# https://github.com/AudriusButkevicius/cli
%global goipath         github.com/AudriusButkevicius/cli
Version:                1.0.0
%global commit          7f561c78b5a4aad858d9fd550c92b5da6d55efbb

%gometa

# Remove in F33
%global godevelheader %{expand:
Obsoletes:      golang-github-AudriusButkevicius-cli-devel < 1.0.0-10
}

%global common_description %{expand:
Cli is simple, fast, and fun package for building command line apps in Go. The
goal is to enable developers to write fast and distributable command line
applications in an expressive way.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        14%{?dist}
Summary:        Small package for building command line apps in Go

License:        MIT
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
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-11.20190703git7f561c7
- Add Obsoletes for old name

* Fri May 31 17:37:04 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.0-10.20190703git7f561c7
- Update to new macros

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9.20140727git7f561c7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.0-8.20140727git7f561c7
- Use forgeautosetup instead of gosetup.

* Thu Aug 30 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.0-7.20140727git7f561c7
- Update to use spec 3.0.

* Wed Jul 25 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.0-6.20140727.git7f561c7
- Include patch to fix building tests with go 1.11.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5.20140727.git7f561c7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4.20140727.git7f561c7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3.20140727.git7f561c7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2.20140727.git7f561c7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 13 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.0-1.20140727.git7f561c7
- First package for Fedora
