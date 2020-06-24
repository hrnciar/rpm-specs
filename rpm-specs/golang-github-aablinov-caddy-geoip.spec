%bcond_without check

# https://github.com/aablinov/caddy-geoip
%global goipath         github.com/aablinov/caddy-geoip
%global commit          c06787a76821ab7852dc1a5219dd5c05d904dce4

%gometa

%global common_description %{expand:
geoip is a Caddy plugin that allow to determine user Geolocation by IP address
using a MaxMind database.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Caddy plugin to resolve user GeoIP data
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/caddyserver/caddy)
BuildRequires:  golang(github.com/caddyserver/caddy/caddyhttp/httpserver)
BuildRequires:  golang(github.com/mmcloughlin/geohash)
BuildRequires:  golang(github.com/oschwald/maxminddb-golang)

%description %{common_description}

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
- Initial package rhbz#1747852
