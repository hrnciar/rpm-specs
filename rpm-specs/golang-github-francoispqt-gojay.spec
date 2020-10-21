# Generated by go2rpm 1
%ifnarch %{ix86} %{arm}
%bcond_without check
%endif

# https://github.com/francoispqt/gojay
%global goipath         github.com/francoispqt/gojay
Version:                1.2.13

%gometa

%global common_description %{expand:
GoJay is a performant JSON encoder/decoder for Golang (currently the most
performant, see benchmarks).

It has a simple API and doesn't use reflection. It relies on small interfaces to
decode/encode structures and slices.

Gojay also comes with powerful stream decoding features and an even faster
Unsafe API.}

%global golicenses      LICENSE
%global godocs          examples README.md

Name:           %{goname}
Release:        2%{?dist}
Summary:        Fastest JSON encoder/decoder with powerful stream API for Golang

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/go-errors/errors)
BuildRequires:  golang(github.com/mailru/easyjson)
BuildRequires:  golang(github.com/mailru/easyjson/jlexer)
BuildRequires:  golang(github.com/mailru/easyjson/jwriter)
BuildRequires:  golang(github.com/viant/toolbox)
BuildRequires:  golang(github.com/viant/toolbox/url)
BuildRequires:  golang(golang.org/x/net/websocket)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/buger/jsonparser)
BuildRequires:  golang(github.com/json-iterator/go)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(github.com/viant/assertly)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in gojay; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck -d gojay/codegen/test/embedded_struct
%endif

%files
%license LICENSE
%doc gojay/README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 13 01:23:04 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.2.13-1
- Initial package
