# Generated by go2rpm
%bcond_without check
%bcond_with network

# https://github.com/wjdp/htmltest
%global goipath         github.com/wjdp/htmltest
Version:                0.12.1

%gometa

%global common_description %{expand:
htmltest runs your HTML output through a series of checks to ensure all your
links, images, scripts references work, your alt tags are filled in, et
cetera.}

%global golicenses      LICENCE
%global godocs          README.md

Name:           htmltest
Release:        1%{?dist}
Summary:        Test generated HTML for problems

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/docopt/docopt-go)
BuildRequires:  golang(github.com/fatih/color) >= 1.7.0
BuildRequires:  golang(github.com/imdario/mergo) >= 0.3.8
BuildRequires:  golang(golang.org/x/net/html)
BuildRequires:  golang(gopkg.in/seborama/govcr.v2) >= 2.4.2
BuildRequires:  golang(gopkg.in/yaml.v2) >= 2.2.7

%if %{with check}
# Tests
BuildRequires:  golang(github.com/daviddengcn/go-assert)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/htmltest %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%if !%{with network}
# Skips:
# - TestAnchorExternalBrokenNoVCR
# - TestAnchorExternalHTTPSMissingChain
# - TestCacheIntegration
# - TestSelfSignedLink
# - TestSelfSignedLinkIgnoreSSLVerify
%global gotestflags %{gotestflags} -run ([^Rkny]|[^io]n|[^i]on|[^t]ion|[^a]tion|[^r]ation|[^n]k|[^i]nk|[^L]ink|[^d]Link|[^f]y)$
%endif
%gocheck
%endif

%files
%doc README.md
%license LICENCE
%{_bindir}/*

%gopkgfiles

%changelog
* Sat Feb 22 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.12.1-1
- Update to latest version

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.11.0-1
- Update to latest version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 21:46:45 EDT 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.10.3-1
- Initial package
