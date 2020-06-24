# Generated by go2rpm
%bcond_without check

# https://github.com/auth0/go-jwt-middleware
%global goipath         github.com/auth0/go-jwt-middleware
%global commit          36081240882bbf356af6efb152969e4b0bcf4456

%gometa

# Remove in F33
%global godevelheader %{expand:
Obsoletes:      golang-github-auth0-go-jwt-middleware-devel < 0.1-11
Obsoletes:      golang-github-auth0-go-jwt-middleware-unit-test-devel < 0.1-11
}

%global common_description %{expand:
A middleware that will check that a JWT is sent on the Authorization header and
will then set the content of the JWT into the user variable of the request.

This module lets you authenticate HTTP requests using JWT tokens in your Go
Programming Language applications. JWTs are typically used to protect API
endpoints, and are often issued using OpenID Connect.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0.1
Release:        15%{?dist}
Summary:        Middleware for Go to check for jwts on http requests

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/dgrijalva/jwt-go)
BuildRequires:  golang(github.com/go-martini/martini)
BuildRequires:  golang(github.com/gorilla/mux)
BuildRequires:  golang(github.com/urfave/negroni)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/smartystreets/goconvey/convey)
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
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 28 00:57:24 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.1-14.20200128git3608124
- Bump to commit 36081240882bbf356af6efb152969e4b0bcf4456

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.1-12.20190622git5493cab
- Add Obsoletes for old name

* Mon Apr 15 22:37:22 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.1-11.20190622git5493cab
- Bump to 5493cabe49f7bfa6e2ec444a09d334d90cd4e2bd

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-10.git8c897f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-9.git8c897f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-8.git8c897f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-7.git8c897f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-6.git8c897f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-5.git8c897f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-4.git8c897f7
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-3.git8c897f7
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-2.git8c897f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 12 2015 lpabon <lpabon@redhat.com> - 0.1-1.git8c897f7
- First package for Fedora

