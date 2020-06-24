%if 0%{?fedora} < 19
%global	rubyabi	1.9.1
%endif

#%%define usescm 1
%undefine	usescm

%{!?python_sitearch:	%global	python_sitearch	%(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

%global	repoid		72126

%global	mainver	2.10.12
%global	prever	2.10.10
#%%define	betaver	-rc1
%undefine	betaver
%define	betarel	%(echo %betaver | sed -e 's|-|_|' | sed -e 's|^_||')

%global	fedoraver	1

%global	enable_python2	1
%if 0%{?fedora} >= 32
%global	enable_python2	0
%endif
%global	enable_python3	0
%if 0%{?fedora} >= 13
# Disable python3 support for now, how to handle NON-utf8 string
# in python3 with skf...
%global	enable_python3	0
%endif

%undefine        _changelog_trimtime

Name:		skf
Version:	%{mainver}
Release:	%{?betaver:0.}%{fedoraver}%{?betaver:.%betarel}%{?dist}.3
Summary:	Utility binary files in Simple Kanji Filter

License:	BSD and MIT and UCD
URL:		http://osdn.jp/projects/skf
Source0:	http://dl.osdn.jp/skf/%{repoid}/skf_%{mainver}%{?betaver}.tar.xz
Source1:	skf-basic-test.sh
Source2:	create-skf-tarball-from-scm.sh

# common BR
BuildRequires:	gcc
BuildRequires:	gettext
# BR for extenstions
BuildRequires:	swig
BuildRequires:	ruby-devel
BuildRequires:	rubygems-devel
%if 0%{?fedora} < 19
BuildRequires:	ruby(abi) = %{rubyabi}
%endif
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl(ExtUtils::Embed)
%if %{enable_python2}
BuildRequires:	python2-devel
%endif
%if %enable_python3
BuildRequires:	python3-devel
%endif
%if 0%{?usescm} >= 1
BuildRequires:	autoconf
%endif

Requires:	%{name}-common = %{version}-%{release}
%if ! %{enable_python2}
Obsoletes:	python2-skf < %{prever}.99
Obsoletes:	skf-python < %{prever}.99
%endif


%package	common
Summary:	Common files for Simple Kanji Filter - i18n kanji converter

%package	ruby
Summary:	Ruby extension module for %{name}
Requires:	%{name}-common = %{version}-%{release}
%if 0%{?fedora} >= 19
Requires:	ruby(release)
%else
Requires:	ruby(abi) = %{rubyabi}
%endif
Provides:	ruby(skf) = %{version}-%{release}

%if 0%{?fedora} >= 27
%package	-n python2-skf
%{?python_provide:%python_provide python2-skf}
# Remove before F30
Provides: %{name}-python = %{version}-%{release}
Provides: %{name}-python%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-python < %{version}-%{release}
%else
%package	python
%endif
Summary:	Python extension module for %{name}
Requires:	%{name}-common = %{version}-%{release}

%if %enable_python3
%package	python3
Summary:	Python3 extension module for %{name}
Requires:	%{name}-common = %{version}-%{release}
%endif

%package	perl
Summary:	Perl extension module for %{name}
Requires:	%{name}-common = %{version}-%{release}
Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This package contains utility binary files in skf.

%description	common
skf is an i18n-capable kanji filter. skf is designed for
reading documents in various languages and codes using kanji
or unicode capable display devices. Like other kanji filters,
skf provides basic Japanese kanji code conversion features, 
include to/from JIS, EUC, Shift-JIS, UCS2, KEIS83 and UTF-7/8,
but also support various international codesets include Korian
and Chinese standard codesets.

Unlike nkf, skf does not provide additional fancy features
like broken jis recovery, but it has support for ISO-8859's,
European domestic sets, JIS X-0212/X-0213 code conversion, 
IBM gaiji support and can add other code supports easily.

This package contains files commonly used by other skf related
packages.

%description	ruby
This package contains Ruby extension module for skf.

%if 0%{?fedora} >= 27
%description	-n python2-skf
%else
%description	python
%endif
This package contains Python extension module for skf.

%if %enable_python3
%description	python3
This package contains Python3 extension module for skf.
%endif

%description	perl
This package contains Perl extension module for skf.

%prep
%setup -q -c -T -a 0
ln -sf %{name}-* main

cp -p %SOURCE1 .

pushd main

%if 0%{?usescm} >= 1
autoconf

mkdir -p doc || :
touch doc/empty

find . -type d -name CVS | sort -r | xargs rm -rf
%endif

## Fixing build error
# Fix pythonext build error on F-14+
%if 0%{?fedora} >= 26
sed -i -e '/python_version=.*substr/s|)-2|)-3|' configure
%else
sed -i -e '/python_version=.*substr/s|7,-3|7,3|' configure
%endif

## configure option, etc
# change optflags, don't strip
# believe upstream
#sed -i.flags -e 's|-Wno-format-security||' configure

## directory change
# change the directory where tables are to be installed
sed -i.table -e "s|^lskfdir=.*$|lskfdir='%{_libdir}/%{name}'|" configure

## documents
# EUC-JP related
sed -i.eucjp -e '/JOMANDIR/d' Makefile.in
popd # from main

# Okay, duplicate main directory
for ext in \
%if %enable_python3
	python3 \
%endif
	ruby perl python
do
	mkdir -p $ext
	cp -pr main/* $ext
done

# change optflags
# add -fno-strict-aliasing
%global	optflags_old	%optflags
%global	optflags	%optflags_old -fno-strict-aliasing

%build
# Parallel make all unsafe

OPTS=""
OPTS="$OPTS --enable-debug"
OPTS="$OPTS --disable-strip"

OPTS="$OPTS --with-ruby_sitearch_dir=%{ruby_vendorarchdir}"

PYTHONOPTS="$OPTS --enable-python2 --with-python_sitearch_dir=%{python2_sitearch}"
%if %enable_python3
PYTHON3OPTS="$OPTS --enable-python3 --with-python_sitearch_dir=%{python3_sitearch}"
%endif

# A. main
pushd main
%configure $OPTS
make -j1
popd

# B. extensions
for ext in \
	ruby perl \
%if %{enable_python2}
	python
%else
	%{nil}
%endif
do
	pushd $ext

    if [ $ext == ruby ] ; then
        export CFLAGS="%optflags $(pkg-config --cflags ruby)"
    fi

	sed -i.py configure -e '\@enable_python3="yes"@d'
	%configure $OPTS $PYTHONOPTS
	unset CFLAGS
	make -j1 ${ext}ext

	# Check if tables generated in each extension are
	# the same as in main
	shopt -s nullglob
	pushd table
	for f in *stb
	do
		cmp --quiet $f ../../main/table/$f || exit 1
	done
	popd
	shopt -u nullglob

	popd
done

# python3
%if %enable_python3
pushd python3
export PYTHON=python3
%configure $OPTS $PYTHON3OPTS
unset CFLAGS
# The following is pythonext, not python3ext
make -j1 pythonext
unset PYTHON
popd
%endif

# tweak find-debuginfo.sh
%if 0%{?fedora} >= 27
%global	debuginfo_subdir	%{name}-%{version}-%{release}.%{?_arch}
%else
%global	debuginfo_subdir	%{?buildsubdir}
%endif
%global	__debug_install_post_old	%__debug_install_post
%global	__debug_install_post		\
	\
	%__debug_install_post_old \
	pushd %{buildroot}%{_prefix}/src/debug/%{debuginfo_subdir} \
	for ext in \\\
		python3 \\\
		ruby python perl \
	do \
		test -d $ext || continue \
		cd $ext \
		for file in * \
		do \
			if test -f ../main/$file \
			then \
				status=$(cmp --quiet $file ../main/$file && echo $? || echo $?) \
				if test $status = 0 ; then \
					ln -sf ../main/$file $file \
				fi \
			fi \
		done \
		cd .. \
	done \
	for ext in \\\
		ruby perl \
	do \
		cd $ext \
		for file in *_table_defs.h \
		do \
			status=$(cmp --quiet $file ../python/$file && echo $? || echo $?) \
			if test $status = 0 ; then \
				ln -sf ../python/$file $file \
			fi \
		done \
		cd .. \
	done \
	popd \
	%{nil}

%install
rm -rf %{buildroot}

OPTS=""
OPTS="${OPTS} DESTDIR=%{buildroot}"
OPTS="${OPTS} INSTALL='install -p'"
OPTS="${OPTS} INSTALL_DATA='install -p -m 0644'"

OPTS="$OPTS JMANDIR=%{_mandir}/ja/man1"

# A. main
eval make -C main ${OPTS} install locale_install

# Kill documents, will install with %%doc
rm -rf %{buildroot}%{_defaultdocdir}

# B. extentions
for ext in ruby \
%if %{enable_python2}
	python
%else
	%{nil}
%endif
do
	eval make -C $ext ${OPTS} ${ext}ext_install
done
## python3
%if %enable_python3
( eval make -C python3 ${OPTS} pythonext_install )
%endif

## perl
pushd perl
mkdir -p %{buildroot}%{perl_vendorarch}/auto/skf
install -cpm 0644 skf.pm %{buildroot}%{perl_vendorarch}
install -cpm 0755 skf.so %{buildroot}%{perl_vendorarch}/auto/skf/skf.so
popd

## Cleanup
%if %{enable_python2}
chmod 0644 %{buildroot}%{python2_sitearch}/skf.py
%endif

%find_lang %{name}

%check
# Setting environ
export PATH=%{buildroot}%{_bindir}:$PATH

export PERL5LIB=%{buildroot}%{perl_vendorarch}
export python2PATH=%{buildroot}%{python2_sitearch}
%if %enable_python3
export python3PATH=%{buildroot}%{python3_sitearch}
%endif
export RUBYLIB=%{buildroot}%{ruby_vendorarchdir}

%if ! %{enable_python2}
export CHECK_PYTHON2=no
%endif

# SOURCE1
sh skf-basic-test.sh

%files
%defattr(-,root,root,-)
%{_bindir}/skf

%{_mandir}/man1/skf.1*
%lang(ja)	%{_mandir}/ja/man1/skf.1*

%files	common	-f %{name}.lang
%defattr(-,root,root,-)
%lang(ja)	%doc	main/CHANGES_ja.txt
%doc	main/README.txt
%doc	main/copyright
%if 0%{?usescm} < 1
%lang(ja)	%doc	main/doc/
%endif

%{_libdir}/%{name}/

%files	ruby
%defattr(-,root,root,-)
%{ruby_vendorarchdir}/skf.so

%if %{enable_python2}
%if 0%{?fedora} >= 27
%files	-n python2-skf
%else
%files	python
%endif
%defattr(-,root,root,-)
%{python2_sitearch}/_skf.so
%{python2_sitearch}/skf.py*
%endif

%if %enable_python3
%files	python3
%defattr(-,root,root,-)
%{python3_sitearch}/_skf.so
%{python3_sitearch}/skf.py*
%endif

%files	perl
%defattr(-,root,root,-)
%{perl_vendorarch}/skf.pm
%{perl_vendorarch}/auto/skf/

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.10.12-1.3
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.12-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.12-1.1
- F-32: rebuild against ruby27

* Wed Jan  1 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.12-1
- 2.10.12

* Tue Nov  5 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.11-1
- 2.10.11
- F-32: drop python2 support

* Tue Jul 30 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.10-1
- 2.10.10

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.9-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.10.9-1.1
- Perl 5.30 rebuild

* Tue Apr  9 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.9-1
- 2.10.9

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.8.2-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.8.2-1.1
- F-30: rebuild against ruby26

* Mon Dec 31 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.8.2-1
- 2.10.8.2

* Fri Sep  7 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.7.1-1
- 2.10.7.1 (ruby binding bugfix release)

* Thu Sep  6 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.7-1
- 2.10.7 (not built actually)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.5-1.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.10.5-1.3
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.5-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 03 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.5-1.1
- F-28: rebuild for ruby25

* Sun Dec 31 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.5-1
- 2.10.5

* Wed Nov 22 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.4-1
- 2.10.4

* Fri Oct 13 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.2-1
- 2.10.2

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.10.1-3.5
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.10.1-3.4
- Python 2 binary package renamed to python2-skf
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-3.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.10.1-3.1
- Perl 5.26 rebuild

* Mon Mar 13 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.1-3
- Modify %%__debug_install_post treaking wrt rpm parallel debuginfo change

* Mon Mar 13 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10.1-2
- 2.10.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10-1
- 2.10

* Wed Jan 11 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10-0.1.rc1.1
- F-26: rebuild for ruby24

* Thu Jan  5 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.10-0.1.rc1
- 2.10-rc1

* Fri Jul 29 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.00.6-1
- 2.00.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00.4-1.2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.00.4-1.1
- Perl 5.24 rebuild

* Wed Feb 10 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.00.4-1
- 2.00.4

* Tue Feb  2 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.00.3-1
- 2.00.3

* Thu Jan 14 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.00.2-2
- F-24: rebuild against ruby23

* Sun Dec 06 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.00.2-1
- 2.00.2

* Mon Jun 23 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.00.1-1
- 2.00.1

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.00-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.00-1.1
- Perl 5.22 rebuild

* Fri May 29 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.00-1
- 2.00

* Sun May  3 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.00-0.5.b2a_2
- 2.00b2a-2

* Sat May  2 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.00-0.4.b2a_1
- 2.00b2a-1

* Fri Jan 16 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.00-0.3.b1_0
- F-22: Rebuild for ruby 2.2

* Tue Jan 13 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.00-0.2.b1_0
- 2.00b1-0

* Sun Jan  4 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.00-0.1.b0_0
- 2.00b0-0

* Sun Nov 23 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.99.10-1
- 1.99.10

* Wed Sep 10 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.99.9-1
- 1.99.9

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.99.8-1.4
- Perl 5.20 rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.99.8-1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.99.8-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 29 2014 Vít Ondruch <vondruch@redhat.com> - 1.99.8-1.1
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Tue Feb  4 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.99.8-1
- 1.99.8

* Mon Dec 30 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.99.7-1
- 1.99.7

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 1.99.6-1.1
- Perl 5.18 rebuild

* Sat Jul 27 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.99.6-1
- 1.99.6

* Fri Jul 26 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.99.5-1
- 1.99.5

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.99.4-1.1
- Perl 5.18 rebuild

* Tue Apr 23 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.99.4-1
- 1.99.4

* Fri Apr 12 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.99.3-1
- 1.99.3

* Wed Mar 27 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.99.2-0.1.cvs20130327T1317
- Try CVS source for ruby 2.0 support

* Sun Mar 17 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.99.1-2
- F-19: rebuild for ruby 2.0.0

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.99.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 15 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.99.1-1
- 1.99.1

* Mon Jan 14 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.99.0-3
- Check if tables generated in each extension are the same as in main
- Detect and strip same files in debuginfo rpm more

* Thu Jan 10 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.99.0-2
- Workaround for gcc48 build failure (dyn_table_gen segfault)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.99.0-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 08 2012 Petr Pisar <ppisar@redhat.com> - 1.99.0-1.1
- Perl 5.16 rebuild

* Mon Apr  2 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.99.0-1
- 1.99.0

* Thu Jan  5 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.99-0.2.alg
- F-17: rebuild against gcc47

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.99-0.1.a1g.1
- Perl mass rebuild

* Thu Mar 24 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 1.99-0.1.a1g
- Try 1.99 a1g

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.97.4-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  9 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.97.4-1
- 1.97.4

* Thu Nov  4 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.97.3-1
- 1.97.3

* Thu Aug 12 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.97.2-1
- 1.97.2
- The method to build python3 binding is now written in the spec file,
  however for now not activate it

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.97.1-2.2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jun 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.97.1-2.1
- Mass rebuild with perl-5.12.0

* Thu Apr  1 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.97.1-2
- 1.97.1

* Thu Mar 25 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.97.0-0.2.a
- Remove useless sed line
- Move man pages to "main" package

* Sat Mar 20 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.97.0-0.1.a
- 1.97.0a
- Initial packaging
