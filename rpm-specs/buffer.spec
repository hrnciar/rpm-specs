#
# $Id$
#
%define debug_package %{nil}

Summary:        This program speeds up writing tapes on remote tape drives
Summary(fr):    Ce programme accélère l'écriture des bandes sur des périphériques distants

Name:           buffer
Version:        1.19
Release:        18%{?dist}
License:        GPL+
Url:            http://hello-penguin.com/software/buffer
Source:         http://hello-penguin.com/software/buffer/%{name}-%{version}.tar.gz
 
Patch0:         01-debian-patches.all.gz
Patch1:         02-fedora-patch.all.gz
Patch2:         03-GPL.patch.all.gz


BuildRequires:  gcc
%description
This is a program designed to speed up writing tapes on remote tape drives.
When this program is put "in the pipe", two processes are started.
One process reads from standard-in and the other writes to standard-out.
Both processes communicate via shared memory.

%description -l fr
Le programme buffer est conçu pour accélérer l'écriture des bandes sur des
périphériques bande distants.
Quand ce programme est utilisé dans un tuyau (pipe), deux processus sont 
démarrés.
Un processus lit depuis l'entrée standard et l'autre écrit vers la sortie 
standard.
Les deux processus communiquent au travers de mémoire partagée.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
make %{?_smp_mflags} CFLAGS="%{optflags} -Dultrix"

%install
install -p -m 755 -D buffer --strip %{buildroot}/%{_bindir}/buffer
install -p -m 644 -D buffer.man %{buildroot}/%{_mandir}/man1/buffer.1

%files
%doc README 
%license COPYING
%{_bindir}/buffer
%{_mandir}/man1/buffer.1*

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 02 2015 Bruno Cornec <bruno@project-builder.org> 1.19-8
- Updated to 1.19-8
- Fix spec file for Fedora conformity (Bruno Cornec/Miroslav Suchý)

* Fri Oct 03 2008 Bruno Cornec <bruno@project-builder.org> 1.19-3
- Updated to 1.19-3
- Fix the french summary (Bruno Cornec)

* Thu Oct 02 2008 Bruno Cornec <bruno@project-builder.org> 1.19-2
- Updated to 1.19-2
- Fix build flags for Fedora conformity (Bruno Cornec)

* Sat Sep 20 2008 Bruno Cornec <bruno@project-builder.org> 1.19-1
- Updated to 1.19-1
- Updated to 1.19 (Bruno Cornec)



