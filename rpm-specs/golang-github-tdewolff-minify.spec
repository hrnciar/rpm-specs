# Generated by go2rpm
%bcond_without check

# https://github.com/tdewolff/minify
%global goipath         github.com/tdewolff/minify
Version:                2.7.4

%gometa

%global common_description %{expand:
Minify is a minifier package written in Go. It provides HTML5, CSS3, JS, JSON,
SVG and XML minifiers and an interface to implement any other minifier.
Minification is the process of removing bytes from a file (such as whitespace)
without changing its output and therefore shrinking its size and speeding up
transmission over the internet and possibly parsing. The implemented minifiers
are designed for high performance.

The core functionality associates mimetypes with minification functions,
allowing embedded resources (like CSS or JS within HTML files) to be minified as
well. Users can add new implementations that are triggered based on a mimetype
(or pattern), or redirect to an external command (like ClosureCompiler,
UglifyCSS, ...).}

%global golicenses      LICENSE.md
%global godocs          README.md README-minify.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Go minifiers for web formats

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  (golang(github.com/dustin/go-humanize) >= 1.0.0 with golang(github.com/dustin/go-humanize) < 2)
BuildRequires:  (golang(github.com/fsnotify/fsnotify) >= 1.4.7 with golang(github.com/fsnotify/fsnotify) < 2)
BuildRequires:  golang(github.com/matryer/try)
BuildRequires:  (golang(github.com/spf13/pflag) >= 1.0.3 with golang(github.com/spf13/pflag) < 2)
BuildRequires:  (golang(github.com/tdewolff/parse)         >= 2.4.2 with golang(github.com/tdewolff/parse)         < 3)
BuildRequires:  (golang(github.com/tdewolff/parse/buffer)  >= 2.4.2 with golang(github.com/tdewolff/parse/buffer)  < 3)
BuildRequires:  (golang(github.com/tdewolff/parse/css)     >= 2.4.2 with golang(github.com/tdewolff/parse/css)     < 3)
BuildRequires:  (golang(github.com/tdewolff/parse/html)    >= 2.4.2 with golang(github.com/tdewolff/parse/html)    < 3)
BuildRequires:  (golang(github.com/tdewolff/parse/js)      >= 2.4.2 with golang(github.com/tdewolff/parse/js)      < 3)
BuildRequires:  (golang(github.com/tdewolff/parse/json)    >= 2.4.2 with golang(github.com/tdewolff/parse/json)    < 3)
BuildRequires:  (golang(github.com/tdewolff/parse/strconv) >= 2.4.2 with golang(github.com/tdewolff/parse/strconv) < 3)
BuildRequires:  (golang(github.com/tdewolff/parse/svg)     >= 2.4.2 with golang(github.com/tdewolff/parse/svg)     < 3)
BuildRequires:  (golang(github.com/tdewolff/parse/xml)     >= 2.4.2 with golang(github.com/tdewolff/parse/xml)     < 3)

%if %{with check}
# Tests
BuildRequires:  (golang(github.com/tdewolff/test) >= 1.0.6 with golang(github.com/tdewolff/test) < 2)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
mv cmd/minify/README.md README-minify.md
# Depend on unversioned tdewolff/parse until Go modules are supported in Fedora
# Provide unversioned import path until Go modules are supported in Fedora
sed -i \
    -e 's|"github.com/tdewolff/parse/v2|"github.com/tdewolff/parse|' \
    -e 's|"github.com/tdewolff/minify/v2|"github.com/tdewolff/minify|' \
    $(find . -name '*.go')

%build
export LDFLAGS='-X main.Version=%{version} '
%gobuild -o %{gobuilddir}/bin/gominify %{goipath}/cmd/minify

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE.md
%doc README.md README-minify.md
%{_bindir}/*

%gopkgfiles

%changelog
* Sat Apr 25 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.7.4-1
- Update to latest version

* Sun Mar 15 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.7.3-1
- Update to latest version

* Sat Feb 15 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.7.2-1
- Update to latest version

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.6.2-1
- Update to latest version

* Tue Nov 26 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.6.0-1
- Update to latest version

* Fri Sep 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.5.2-1
- Update to latest version

* Sun Aug 18 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.5.1-1
- Update to latest version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 22:53:20 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.5.0-2
- Update to new macros

* Fri May 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.5.0-1
- Update to latest version

* Tue Apr 23 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.4.0-1
- Update to latest version

* Sat Mar 02 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.3.8-2
- Uncomment test BRs
- Depend on unversioned tdewolff/parse until Go modules are supported in Fedora

* Sun Feb 10 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.3.8-1
- First package for Fedora