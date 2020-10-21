# Generated by go2rpm
%bcond_without check

# https://github.com/nicksnyder/go-i18n
%global goipath         github.com/nicksnyder/go-i18n
%global goipathsex      github.com/nicksnyder/go-i18n/v2
Epoch:                  1
Version:                1.10.1

%gometa

# Remove in F33
%global godevelheader %{expand:
Obsoletes:      golang-github-nicksnyder-go-i18n-devel < 1.10.0-7
Obsoletes:      golang-github-nicksnyder-go-i18n-unit-test-devel < 1.10.0-7
}

%global common_description %{expand:
go-i18n is a Go package and a command that helps you translate Go programs into
multiple languages.

 - Supports pluralized strings for all 200+ languages in the Unicode Common
   Locale Data Repository (CLDR).
    - Code and tests are automatically generated from CLDR data.
 - Supports strings with named variables using text/template syntax.
 - Supports message files of any format (e.g. JSON, TOML, YAML, etc.).
 - Documented and tested!}

%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md dev.md

Name:           %{goname}
Release:        4%{?dist}
Summary:        Translate your Go program into multiple languages

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/BurntSushi/toml)
BuildRequires:  golang(github.com/pelletier/go-toml)
BuildRequires:  golang(golang.org/x/text/language)
BuildRequires:  golang(gopkg.in/yaml.v2)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall
rm -r %{buildroot}%{gopath}/src/%{goipath}/v2
sed -i -e '/v2/d' %{gorpmname %{goipath}}-%{gofilelist}

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.10.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.10.1-1
- Downgrade to latest v1 release; v2 can be found in golang-github-nicksnyder-i18n-2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.2-1
- Update to latest version

* Tue Jul 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.0.0-2
- Add binary subpackage
- Add Obsoletes for old name

* Thu May 23 18:53:45 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.0.0-1
- Release 2.0.0

* Tue Feb 19 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.10.0-1
- First package for Fedora
