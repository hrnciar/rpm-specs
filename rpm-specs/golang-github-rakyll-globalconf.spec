# Generated by go2rpm
%bcond_without check

# https://github.com/rakyll/globalconf
%global goipath         github.com/rakyll/globalconf
%global commit          87f8127c421f4ccdaac33c9fca40c305c654f1de

%gometa

%global common_description %{expand:
Effortlessly persist/retrieve flags of your Golang programs. If you need global
configuration instead of requiring user always to set command line flags, you
are looking at the right package. globalconf allows your users to not only
provide flags, but config files and environment variables as well.}

%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.15%{?dist}
Summary:        Persist flag values into an ini file

License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/glacjay/goini)

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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 17:44:18 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.13.20190602git87f8127
- Bump to commit 87f8127c421f4ccdaac33c9fca40c305c654f1de

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.git415abc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.git415abc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.git415abc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git415abc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git415abc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git415abc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.git415abc3
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.git415abc3
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git415abc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Aug 07 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.3.git415abc3
- Update spec file to spec-2.0
  resolves: #1250499

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.git415abc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Dec 27 2014 jchaloup <jchaloup@redhat.com> - 0-0.1.git415abc3
- First package for Fedora
  resolves: #1177487