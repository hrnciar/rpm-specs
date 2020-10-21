# Generated by go2rpm 1
%bcond_without check

# https://github.com/ssgelm/cookiejarparser
%global goipath         github.com/ssgelm/cookiejarparser
Version:                1.0.1

%gometa

%global common_description %{expand:
A Go library that parses a curl (netscape) cookiejar file into a Go
http.CookieJar.}

%global golicenses      LICENSE.md
%global godocs          README.md data/cookies.txt

Name:           %{goname}
Release:        3%{?dist}
Summary:        Parses a curl cookiejar file into a Go http.CookieJar

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/net/publicsuffix)

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
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 01 21:46:44 EST 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.1-1
- Initial package
