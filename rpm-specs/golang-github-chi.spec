# Generated by go2rpm
# local network access fails on s390x
%ifnarch s390x
%bcond_without check
%endif

# https://github.com/go-chi/chi
%global goipath         github.com/go-chi/chi
Version:                4.0.3

%gometa

%global goaltipaths     github.com/pressly/chi

%global common_description %{expand:
Chi is a lightweight, idiomatic and composable router for building Go HTTP
services. It's especially good at helping you write large REST API services that
are kept maintainable as your project grows and changes. chi is built on the new
context package introduced in Go 1.7 to handle signaling, cancelation and
request-scoped values across a handler chain.

The focus of the project has been to seek out an elegant and comfortable design
for writing REST API servers, written during the development of the Pressly API
service that powers our public API service, which in turn powers all of our
client-side applications.}

%global golicenses      LICENSE
%global godocs          _examples CHANGELOG.md CONTRIBUTING.md README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Lightweight, idiomatic and composable router for building Go HTTP services

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(golang.org/x/net/http2)
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
* Wed Jan 29 17:24:14 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 4.0.3-1
- Update to 4.0.3

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 07 18:07:40 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 4.0.2-1
- Initial package
