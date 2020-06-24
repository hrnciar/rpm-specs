Name: puzzles
Version: 9023
Release: 22%{?dist}
Summary: A collection of one-player puzzle games

License: MIT
URL: http://www.chiark.greenend.org.uk/~sgtatham/puzzles/
Source0: http://www.chiark.greenend.org.uk/~sgtatham/puzzles/puzzles-r%{version}.tar.gz
Source1: template.desktop
Patch0:  puzzles-math.patch

BuildRequires:  gcc
BuildRequires: gtk2-devel, perl-interpreter, desktop-file-utils

%description
This is a collection of small desktop toys, little games that you can 
pop up in a window and play for two or three minutes while you take a 
break from whatever else you were doing.

%prep
%setup -q -n puzzles-r%{version}
%patch0
# uses the fedora command line instead of the one hardcoded in the makefile
# -g is the last option that is not application specific. 
# TODO: THIS IS UGLY, NEW VERSIONS COULD MAKE THIS STOP WORKING
sed -i -e "s|CFLAGS := .*-g|CFLAGS := %{optflags}|" Makefile

iconv -f ISO88591 -t UTF8< LICENCE > LICENSE


%build

make %{?_smp_mflags}


%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/puzzles
cp -a icons/*-32d24.png $RPM_BUILD_ROOT/%{_datadir}/puzzles

make install prefix=%{_prefix} gamesdir=%{_bindir} bindir=%{_bindir} DESTDIR=$RPM_BUILD_ROOT

# create all the desktop files needed.
path=$RPM_BUILD_ROOT/%{_bindir}
for i in $path/*; do 
	base=`basename $i`
	name=`perl -e 'print ucfirst($ARGV[0])' "$base"`
	command=puzzle-$base

	mv $i $path/$command

	sed -e "s/<NAME>/$name/g;s!<EXEC>!%{_bindir}/$command!g;s!<ICON>!%{_datadir}/puzzles/$base-32d24.png!g" %{SOURCE1} > puzzle-$base.desktop
	desktop-file-install \
		--dir=${RPM_BUILD_ROOT}%{_datadir}/applications/ \
		$command.desktop
done


%files
%doc README HACKING puzzles.txt
%license LICENSE
%{_bindir}/*
%{_datadir}/puzzles
%{_datadir}/applications/*


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9023-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9023-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9023-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9023-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9023-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9023-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9023-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9023-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 9023-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jun 21 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 9023-13
- Use '|' as pattern-delimiter in sed expression (Fix FTFBS).
- Add %%license.
- Modernize spec.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9023-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9023-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9023-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9023-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar  6 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 9023-8
- Remove vendor prefix from desktop files in F19+ https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9023-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9023-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jan 29 2012 Bruno Wolff III <bruno@wolff.to> - 9023-5
- Link with math library

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9023-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 9023-3
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9023-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 13 2010 Victor Bogado <victor@bogado.net> 9023
- New upstream release.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8596-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

*Mon Jun 22 2009  Victor Bogado <victor@bogado.net> 8596-1
- updating to a new upstream version

*Thu Dec 11 2008  Victor Bogado <victor@bogado.net> 8365-1
- New updastream version

*Mon Oct 27 2008  Victor Bogado <victor@bogado.net> 8200-3
- Build-Requires should have desktop-file-utils
- Description should start with uppercase
- iconv goes now in prep area
- fixed mistakes in the versions of the change log
- Names on the menu should start with an upper-case

*Mon Oct 20 2008 Victor Bogado <victor@bogado.net> 8200-2
- Fixing problem with desktop files.

*Mon Oct 20 2008 Victor Bogado <victor@bogado.net> 8200-1
- Suggestion made by reviewer Sergio Pascual <sergio.pasra@gmail.com>.
- rename all the binaries.
- rename desktop files to follow the binary name.
- adding LICENCE (renamed to LICENSE) to docs.
- sed "in place", better coding.
- removing sed out of build-requires.
- Updated to last upstream version.

*Mon Sep 01 2008 Victor Bogado <victor@bogado.net> 8149-1
- initial spec
