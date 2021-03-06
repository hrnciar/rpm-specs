# Generated by go2rpm 1
%bcond_without check

# https://github.com/nbutton23/zxcvbn-go
%global goipath         github.com/nbutton23/zxcvbn-go
Version:                0.1
%global commit          ae427f1e4c1d66674cc457c6c3822de13ccb8777

%gometa

%global common_description %{expand:
Zxcvbn password complexity algorithm in golang.}

%global golicenses      LICENSE.txt
%global godocs          README.md

Name:           %{goname}
Release:        3%{?dist}
Summary:        Zxcvbn password complexity algorithm

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

%build
for cmd in testapp; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Apr 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1-1.20200404gitae427f1
- Initial package

