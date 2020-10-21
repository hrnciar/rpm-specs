# Generated by go2rpm
%bcond_without check

# https://github.com/aclements/go-gg
%global goipath         github.com/aclements/go-gg
%global commit          abd1f791f5ee99465ee7cffe771436379d6cee5a

%gometa

%global common_description %{expand:
Gg is a plotting package for Go inspired by the Grammar of Graphics.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.7%{?dist}
Summary:        Plotting package for Go

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
Patch0:         0001-Fix-Sprintf-error-with-time-values.patch
Patch1:         0002-Add-missing-format-in-Fatalf.patch

BuildRequires:  golang(github.com/aclements/go-moremath/fit)
BuildRequires:  golang(github.com/aclements/go-moremath/scale)
BuildRequires:  golang(github.com/aclements/go-moremath/stats)
BuildRequires:  golang(github.com/aclements/go-moremath/vec)
BuildRequires:  golang(github.com/ajstarks/svgo)

%description
%{common_description}

%gopkg

%prep
%goprep
%patch0 -p1
%patch1 -p1

%install
%gopkginstall

%if %{with check}
%check
# new_test.go fails
# https://github.com/aclements/go-gg/issues/11
%gocheck -d "table"
%endif

%gopkgfiles

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 16 21:43:32 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20180422gitabd1f79
- Update to new macros

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gitabd1f79
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitabd1f79
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 23 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180422gitabd1f79
- First package for Fedora
