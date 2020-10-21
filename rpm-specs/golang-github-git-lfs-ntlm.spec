# Generated by go2rpm 1
%bcond_without check

# https://github.com/git-lfs/go-ntlm
%global goipath         github.com/git-lfs/go-ntlm
%global commit          c5056e7fa0664ea69eed654a9618fa5e342dc347

%gometa

%global common_description %{expand:
This is a native implementation of NTLM for Go that was implemented using the
Microsoft MS-NLMP documentation available at
http://msdn.microsoft.com/en-us/library/cc236621.aspx. The library is currently
in use and has been tested with connectionless NTLMv1 and v2 with and without
extended session security.}

%global golicenses      License ntlm/md4/LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        NTLM Implementation for Go

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

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
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 18 18:07:39 EDT 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.1.20190827gitc5056e7
- Initial package
