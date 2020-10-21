# Generated by go2rpm 1
%bcond_without check

# https://github.com/projectdiscovery/subfinder
%global goipath         github.com/projectdiscovery/subfinder
Version:                2.3.5
%global tag             2.3.5

%gometa

%global common_description %{expand:
Subfinder is a subdomain discovery tool that discovers valid subdomains for
websites. Designed as a passive framework to be useful for bug bounties and
safe for penetration testing.}

%global golicenses      LICENSE
%global godocs          ISSUE_TEMPLATE.md THANKS.md README.md DISCLAIMER.md

Name:           subfinder
Release:        3%{?dist}
Summary:        Subdomain discovery tool

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/json-iterator/go)
BuildRequires:  golang(github.com/lib/pq)
BuildRequires:  golang(github.com/m-mizutani/urlscan-go/urlscan)
BuildRequires:  golang(github.com/miekg/dns)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/projectdiscovery/gologger)
BuildRequires:  golang(github.com/rs/xid)
BuildRequires:  golang(gopkg.in/yaml.v3)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in cmd/* ; do
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
%doc ISSUE_TEMPLATE.md THANKS.md README.md DISCLAIMER.md
%{_bindir}/*

%gopkgfiles

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.3.5-1
- Update to latest upstream release 2.3.5

* Sun May 24 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.3.4-1
- Initial package

