Name:		duff
Version:	0.5.2
Release:	19%{?dist}
Summary:	Quickly find duplicate files

License:	zlib
URL:		http://duff.sourceforge.net/
Source0:	http://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-%{version}.tar.gz
Patch1:		duff-linking-to-shared-library-sha.patch
Patch2:		duff-remove-docs-of-sha.patch
BuildRequires:  gcc
BuildRequires:	sha-devel
BuildRequires:	autoconf
BuildRequires:	automake

%description
Duff is a command-line utility for quickly finding duplicates in a given set of
files


%prep
%setup -q
#Remove bundled sha and unnecessary files
rm -rf src/sha*
rm -rf autom4te.cache
rm -rf README.SHA
%patch1 -p1
%patch2 -p1

%build
autoreconf -fi
autoheader
CFLAGS="%{optflags} -I/usr/include/sha"
export CFLAGS
%configure \
	--disable-rpath
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} INSTALL="install -p" CP="cp -p" install
%find_lang %{name}
find %{buildroot} -name 'join-duplicates.sh' | xargs chmod 0755

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_bindir}/duff
%dir %{_datadir}/duff
%{_datadir}/duff/join-duplicates.sh
%{_docdir}/duff
%{_mandir}/man1/duff.1*


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 25 2012 Eduardo Echeverria  <echevemaster@gmail.com> - 0.5.2-5
- Added %%{datadir}/duff to spec
- Remove non-existent tests 

* Thu Nov 01 2012 Eduardo Echeverria  <echevemaster@gmail.com> - 0.5.2-4
- Remove bundled sha files
- Remove unnecessary buildroot
- Remove %%clean 
- Add patch for linking to shared libraries of sha 

* Sun Sep 16 2012 Eduardo Echeverria  <echevemaster@gmail.com> - 0.5.2-3
- Remove rm -rf in section clean

* Sun Sep 16 2012 Eduardo Echeverria  <echevemaster@gmail.com> - 0.5.2-2
- Remove glibc-devel of BuildRequires
- Remove autoconf, autoconf, libtool

* Sat Sep 15 2012 Eduardo Echeverria  <echevemaster@gmail.com> - 0.5.2-1
- Initial packaging
