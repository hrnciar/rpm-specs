# Generated by go2rpm 1
%bcond_without check

# https://github.com/labstack/echo
%global goipath         github.com/labstack/echo/v4
%global forgeurl        https://github.com/labstack/echo
Version:                4.1.16

%gometa

%global common_description %{expand:
High performance, minimalist Go web framework.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        High performance, minimalist Go web framework

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/dgrijalva/jwt-go)
BuildRequires:  golang(github.com/labstack/gommon/bytes)
BuildRequires:  golang(github.com/labstack/gommon/color)
BuildRequires:  golang(github.com/labstack/gommon/log)
BuildRequires:  golang(github.com/labstack/gommon/random)
BuildRequires:  golang(github.com/valyala/fasttemplate)
BuildRequires:  golang(golang.org/x/crypto/acme)
BuildRequires:  golang(golang.org/x/crypto/acme/autocert)
BuildRequires:  golang(golang.org/x/net/http2)
BuildRequires:  golang(golang.org/x/net/http2/h2c)

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

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Wed Aug 26 2020 Ondřej Budai <obudai@redhat.com> - 4.1.16-1
- Initial package
