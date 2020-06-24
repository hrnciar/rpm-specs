# Generated by go2rpm
%bcond_without check

# https://github.com/daviddengcn/go-algs
%global goipath         github.com/daviddengcn/go-algs
%global commit          fe23fabd9d0670e4675326040ba7c285c7117b4c

%gometa

%global common_description %{expand:
Some algorithms in go: maxflow(min-cuts or graph-cuts), edit-distance.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Maxflow and edit-distance algorithms in Go

License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/golangplus/testing/assert)
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
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 20:48:12 EDT 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.1.20190711gitfe23fab
- Initial package