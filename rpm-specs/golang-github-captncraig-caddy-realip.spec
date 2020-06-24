%bcond_without check

%global goipath         github.com/captncraig/caddy-realip
%global commit          6df827e22ab8cd5ea90e0844ff29cf62b95127f9

%gometa

%global golicenses      LICENSE
%global godocs          README.md

%global common_description %{expand:
Middleware for restoring real ip information when running caddy behind a proxy.
Will allow other middlewares to simply use r.RemoteAddr instead of decoding
X-Forwarded-For themselves. Analogous to the realip_module in nginx.}

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Real-IP middleware for caddy
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/caddyserver/caddy)
BuildRequires:  golang(github.com/caddyserver/caddy/caddyhttp/httpserver)

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
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 31 2019 Carl George <carl@george.computer> - 0-0.1
- Initial package rhbz#1747853
