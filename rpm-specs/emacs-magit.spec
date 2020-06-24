%define pkg magit
%define pkgname Magit

%if %($(pkg-config emacs) ; echo $?)
%define emacs_version 22.1
%define emacs_lispdir %{_datadir}/emacs/site-lisp
%define emacs_startdir %{_datadir}/emacs/site-lisp/site-start.d
%else
%define emacs_version %(pkg-config emacs --modversion)
%define emacs_lispdir %(pkg-config emacs --variable sitepkglispdir)
%define emacs_startdir %(pkg-config emacs --variable sitestartdir)
%endif

Name:           emacs-%{pkg}
Version:        1.2.2
Release:        12%{?dist}
Summary:        Emacs interface to the most common Git operations

License:        GPLv3+ and GFDL+
URL:            http://magit.github.com/magit/

Source0:        https://github.com/magit/magit/releases/download/%{version}/magit-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  emacs emacs-el texinfo
Requires:       emacs(bin) >= %{emacs_version}
Obsoletes:      emacs-%{pkg}-el < %{version}-%{release}
Provides:       emacs-%{pkg}-el = %{version}-%{release}

%description
%{pkgname} is an add-on package for GNU Emacs. It is an interface to
the Git source-code management system that aims to make the most
common operations convenient.

%prep
%setup -q -n magit-%{version}

%build
make

%install
make install DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix}

# clean up after magit's installer's assumptions
mkdir -p $RPM_BUILD_ROOT%{emacs_startdir}
mv $RPM_BUILD_ROOT/etc/emacs/site-start.d/50magit.el \
   $RPM_BUILD_ROOT%{emacs_startdir}/emacs-magit-mode.el
mkdir -p $RPM_BUILD_ROOT%{emacs_lispdir}/%{pkg}
mv $RPM_BUILD_ROOT%{emacs_lispdir}/*.el{,c} \
   $RPM_BUILD_ROOT%{emacs_lispdir}/%{pkg}
gzip -9 < magit.info > $RPM_BUILD_ROOT%{_infodir}/magit.info.*
rm $RPM_BUILD_ROOT%{_infodir}/dir

%files
# no license file included
%doc README.md
%{emacs_lispdir}/%{pkg}
%{emacs_startdir}/*.el
%{_infodir}/magit.info.*


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Björn Esser <besser82@fedoraproject.org> - 1.2.2-10
- Remove hardcoded gzip suffix from GNU info pages

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 15 2017 Jens Petersen <petersen@redhat.com> - 1.2.2-5
- drop the el subpackage (#1234540)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jan  4 2015 Jens Petersen <petersen@redhat.com> - 1.2.2-1
- update to 1.2.2 which works with emacs-24.4 (#1172690)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 10 2013 Tom Moertel <tom@moertel.com> - 1.2.0-1
- Update to upstream version 1.2.0

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan 25 2012 Tom Moertel <tom@moertel.com> - 1.1.1-1
- Update to upstream 1.1.1

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri May 13 2011 Tom Moertel <tom@moertel.com> - 1.0.0-1
- Updated to upstream 1.0.0

* Wed Aug  4 2010 Tom Moertel <tom@moertel.com> - 0.8.2-1
- Updated to upstream 0.8.2

* Wed Aug 26 2009 Tom Moertel <tom@moertel.com> - 0.7-6
- Updated for Magit 0.7 final release (note: upstream removed FDL from tarball)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-5.20090122git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-4.20090122git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 29 2009  <tom@moertel.com> - 0.7-3.20090122git
- Added missing build dependency: texinfo

* Tue Jan 27 2009  <tom@moertel.com> - 0.7-2.20090122git
- Made fixes per Fedora packaging review (thanks Jerry James)

* Fri Jan 23 2009  <tom@moertel.com> - 0.7-1.20090122git
- Initial packaging.
