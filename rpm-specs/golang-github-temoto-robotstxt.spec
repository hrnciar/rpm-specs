# Generated by go2rpm 1
%bcond_without check

# https://github.com/temoto/robotstxt
%global goipath         github.com/temoto/robotstxt
Version:                1.1.1

%gometa

%global common_description %{expand:
The robots.txt exclusion protocol implementation for Go language.}

%global golicenses      LICENSE
%global godocs          README.rst

Name:           %{goname}
Release:        2%{?dist}
Summary:        Robots.txt exclusion protocol implementation

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in robots.txt-check; do
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
%license LICENSE
%doc README.rst
%{_bindir}/*

%gopkgfiles

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.1.1-1
- Initial package

