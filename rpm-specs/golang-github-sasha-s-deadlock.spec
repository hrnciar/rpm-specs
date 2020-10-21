# Generated by go2rpm
%bcond_without check

# https://github.com/sasha-s/go-deadlock
%global goipath         github.com/sasha-s/go-deadlock
Version:                0.2.0
%global commit          1595213edefa28ca5047b00340c63557f9c051d0

%gometa

# Remove in F33
%global godevelheader %{expand:
Obsoletes:      golang-github-sasha-s-go-deadlock-devel < 0.2.0-11
}

%global common_description %{expand:
Go-deadlock provides (RW)Mutex drop-in replacements for sync.(RW)Mutex..}

%global golicenses      LICENSE
%global godocs          Readme.md

Name:           %{goname}
Release:        14%{?dist}
Summary:        Online deadlock detection in Go

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/petermattis/goid)

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
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.0-11.20190703git1595213
- Add Obsoletes for old name

* Tue May 28 22:55:55 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.0-10.20190703git1595213
- Bump to commit 1595213edefa28ca5047b00340c63557f9c051d0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-9.20180822gitd68e2bc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.0-8.20180822gitd68e2bc
- Use forgeautosetup instead of gosetup.

* Sun Sep 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.0-7.20180822gitd68e2bc
- Bump to commit d68e2bc.
- Update to use spec 3.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.0-4
- Add another upstream patch to fix lock/unlock ordering.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.0-3
- Add upstream patch to fix a potential race condition.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.0-1
- Update to version 0.2.0.

* Sat Dec 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0-1.20171130.git03d40e5
- Bump to commit 03d40e5.

* Tue Sep 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0-0.5.git565eb44
- Bump to commit 565eb44.

* Mon Aug 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0-0.4.git3410008
- Rebuild for golang(github.com/petermattis/goid) commit 0ded858.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-0.3.git3410008
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-0.2.git3410008
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0-0.1.git3410008
- First package for Fedora
