# Generated by go2rpm 1
%bcond_without check

# https://github.com/blakesmith/ar
%global goipath         github.com/blakesmith/ar
%global commit          809d4375e1fb5bb262c159fc3ec2e7a86a8bfd28

%gometa

%global common_description %{expand:
Golang ar archive file library.}

%global golicenses      COPYING
%global godocs          README.md fixtures/hello.txt fixtures/lamp.txt

Name:           %{goname}
Version:        0
Release:        0.5%{?dist}
Summary:        Golang ar archive file library

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
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.3.20190718git809d437
- Update to latest Go macros

* Sun May 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.2.20190505git809d437
- Update to latest commit

* Sat Apr 27 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.1.20190427git8bd4349
- Initial package
