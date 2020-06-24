%global _hardened_build 1
%global cmake_pkg cmake
%if 0%{?rhel}
%if 0%{?rhel} < 7
%global cmake_pkg cmake28
%global legacy_el 1
%endif
%endif

Name:		zbackup
Version:	1.4.4
Release:	18%{?dist}
Summary:	A versatile deduplicating backup tool

License:	GPLv2+ with exceptions
URL:		http://zbackup.org/
Source0:	https://github.com/zbackup/zbackup/archive/%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:	%{cmake_pkg} >= 2.8.2
BuildRequires:	xz-devel
BuildRequires:	openssl-devel
BuildRequires:	protobuf-devel
BuildRequires:	zlib-devel
BuildRequires:	lzo-devel
BuildRequires:	pandoc

%description
zbackup is a globally-deduplicating backup tool, based on the ideas
found in rsync. Feed a large .tar into it, and it will store duplicate
regions of it only once, then compress and optionally encrypt the
result. Feed another .tar file, and it will also re-use any data found
in any previous backups. This way only new changes are stored, and as
long as the files are not very different, the amount of storage
required is very low.

%prep
%setup -q

%build
mkdir -p objdir tartool/objdir
pushd objdir
%{?cmake28}%{!?cmake28:%{?cmake}} ..
make %{?_smp_mflags}
popd
pushd tartool/objdir
%{?cmake28}%{!?cmake28:%{?cmake}} ..
make %{?_smp_mflags}
popd

%install
%if 0%{?legacy_el}
rm -rf %{buildroot}
%endif
make install -C objdir DESTDIR=%{buildroot}
install tartool/objdir/tartool %{buildroot}%{_bindir}/
%if 0%{?legacy_el}
grep -v travis README.md | pandoc -s -f markdown -t man -o %{name}.1 \
-V title=%{name} -V section=1 -V date="$(LANG=C date -d @$(stat -c'%Z' README.md) +'%B %d, %Y')"
%else
grep -v travis README.md | pandoc -s -f markdown_github -t man -o %{name}.1 \
-V title=%{name} -V section=1 -V date="$(LANG=C date -d @$(stat -c'%Z' README.md) +'%B %d, %Y')"
%endif
install -D -m 644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
ln -s %{name}.1 %{buildroot}%{_mandir}/man1/tartool.1

%files
%{_bindir}/*
%{_mandir}/man1/*.1.*
%if 0%{?legacy_el}
%doc LICENSE LICENSE-GPL* CONTRIBUTORS
%else
%license LICENSE LICENSE-GPL*
%doc CONTRIBUTORS
%endif

%changelog
* Sun Jun 14 2020 Adrian Reber <adrian@lisas.de> - 1.4.4-18
- Rebuilt for protobuf 3.12

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Orion Poplawski <orion@nwra.com> - 1.4.4-16
- Rebuild for protobuf 3.11

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.4-13
- Rebuild for protobuf 3.6

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 29 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.4.4-10
- Rebuild for protobuf 3.5

* Mon Nov 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.4-9
- Rebuild for protobuf 3.4

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Orion Poplawski <orion@cora.nwra.com> - 1.4.4-6
- Rebuild for protobuf 3.3.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 26 2017 Orion Poplawski <orion@cora.nwra.com> - 1.4.4-4
- Rebuild for protobuf 3.2.0

* Sat Nov 19 2016 Orion Poplawski <orion@cora.nwra.com> - 1.4.4-3
- Rebuild for protobuf 3.1.0

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 21 2015 Vladimir Stackov <amigo.elite at gmail dot com> - 1.4.4-1
- Version bumped to 1.4.4

* Wed Aug 19 2015 Vladimir Stackov <amigo.elite at gmail dot com> - 1.4.3-1
- Version bumped to 1.4.3

* Fri Jul 31 2015 Vladimir Stackov <amigo.elite at gmail dot com> - 1.4.2-1
- Version bumped to 1.4.2

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 23 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4.1-2
- Rebuild for protobuf soname bump

* Wed Jan 07 2015 Vladimir Stackov <amigo.elite at gmail dot com> - 1.4.1-1
- Version bumped to 1.4.1
- Added macroses for EL6

* Fri Dec 19 2014 Vladimir Stackov <amigo.elite at gmail dot com> - 1.3-4
- Modified in appliance with rhbz#1172525

* Fri Dec 12 2014 Vladimir Stackov <amigo.elite at gmail dot com> - 1.3-3
- Produce hardened binaries

* Thu Dec 11 2014 Vladimir Stackov <amigo.elite at gmail dot com> - 1.3-2
- Modified in appliance with rhbz#1172525
- Added tartool

* Wed Dec 10 2014 Vladimir Stackov <amigo.elite at gmail dot com> - 1.3-1
- Initial version of the package
