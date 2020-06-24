Name:		progress
Version:	0.14
Release:	5%{?dist}
Summary:	Coreutils Viewer

License:	GPLv3
URL:		https://github.com/Xfennec/%{name}
Source0:	https://github.com/Xfennec/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:	ncurses-devel

%if (0%{?fedora} && 0%{?fedora} <= 26) || (0%{?rhel} && 0%{?rhel} <= 9)
Obsoletes: cv <= 0.8-3
Provides: cv == %{version}-%{release}
%endif # (0%{?fedora} && 0%{?fedora} <= 26) || (0%{?rhel} && 0%{?rhel} <= 9)

%description
Progress can be described as a Tiny Dirty Linux Only* C command that
looks for coreutils basic commands (cp, mv, dd, tar, gzip/gunzip, cat, ...)
currently running on your system and displays the percentage of copied data.

%prep
%setup -q

%build
CFLAGS="%{?optflags}"			\
LFLAGS="%{?__global_ldflags}"	\
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}
install -pm 0755 %{name} %{buildroot}%{_bindir}/%{name}

mkdir -p %{buildroot}%{_mandir}/man1
install -pm 0644 *.1 %{buildroot}%{_mandir}/man1

%files
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 8
%license LICENSE
%else  # 0%{?fedora} >= 21 || 0%{?rhel} >= 8
%doc LICENSE
%endif # 0%{?fedora} >= 21 || 0%{?rhel} >= 8
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/*.1*

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 21 2018 Florian Lehner <dev@der-flo.net> - 0.14-2
- Add gcc as BuildRequire

* Sat Jul 21 2018 Florian Lehner <dev@der-flo.net> - 0.14-1
- Update to new Version

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 30 2016 Forian Lehner <dev@der-flo.net> 0.13.1-1
- Update to 0.13.1

* Sun Mar 20 2016 Florian Lehner <dev@der-flo.net> 0.13-1
- Update to 0.13

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Florian Lehner <dev@der-flo.net> 0.12.1-1
- Update to new Version

* Mon Aug 31 2015 Florian Lehner <dev@der-flo.net> 0.9-1
- Update to new Version

* Tue Aug  4 2015 Florian Lehner <dev@der-flo.net> 0.8-2
- Use license-Macro
- Add missing Obsoletes / Provides

* Mon Aug  3 2015 Florian Lehner <dev@der-flo.net> 0.8-1
- Rename from cv to progress
- Update to new Version

* Wed Jun 24 2015 Florian Lehner <dev@der-flo.net> 0.7-1
- Update to new Version

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Feb 23 2015 Florian Lehner <dev@der-flo.net> 0.6-1
- Update to new Version

* Wed Sep  3 2014 Florian Lehner <dev@der-flo.net> 0.5.1-1
- Update to new version

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug 11 2014 Florian Lehner <dev@der-flo.net> 0.4.1-4
- Unset __hardened_build
- Rename LDFLAGS to LFLAGS

* Sun Aug 10 2014 Florian Lehner <dev@der-flo.net> 0.4.1-3
- Use patch from upstream to consider already set flags
- Use patch from upstream to fix overrides in Makefile
- Use patch from upstream toa add manpage for cv
- Add README.md to doc-section

* Sun Aug 10 2014 Florian Lehner <dev@der-flo.net> 0.4.1-2
- Appending CFLAGS and LDFLAGS instead of overriding it

* Sat Aug  9 2014 Florian Lehner <dev@der-flo.net> 0.4.1-1
- Initial packaging (#1128378)
