%global	gem_name	vte3
%global	glib_min_ver	3.0.8

%undefine        _changelog_trimtime

Summary:	Ruby binding of VTE
Name:		rubygem-%{gem_name}
Version:	3.4.1
Release:	2%{?dist}

License:	LGPLv2+
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://raw.github.com/ruby-gnome2/ruby-gnome2/master/vte3/COPYING.LIB
# Renamed to avoid overwrite on SOURCE dir
Source1:	COPYING.LIB.vte3

%if 0%{?fedora} >= 28
BuildRequires:	vte291
%else
BuildRequires:	vte3
%endif
BuildRequires:	ruby-devel
BuildRequires:	rubygems-devel
BuildRequires:	rubygem-pango-devel
BuildRequires:	rubygem-gtk3
BuildRequires:	rubygem-glib2-devel >= %{glib_min_ver}
BuildRequires:	rubygem(test-unit)
BuildRequires:	%{_bindir}/xvfb-run
%if 0%{?fedora} >= 28
Requires:		vte291
%else
Requires:	vte3
%endif

Obsoletes:		rubygem-vte3-devel < 2.99
Provides:		rubygem-vte3-devel = 2.99

BuildArch:		noarch

%description
Ruby/VTE3 is a Ruby binding of VTE .

%package	devel
Summary:	Ruby/VTE3 development environment
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for building a extension library for the
rubygem-%{gem_name} .

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for %{name} .

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}

# patches

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

# Relax the version dependency
sed -i -e 's|= 3\.4\.1|>= 3.4.1|' %{gem_name}.gemspec

# Add license text
install -cpm 644 %{SOURCE1} ./COPYING.LIB
FREEZE=""
if grep -q '"Rakefile"\.freeze' %{gem_name}.gemspec
then
	FREEZE=".freeze"
fi

sed -i -e "/files =/s|\(\"Rakefile\"${FREEZE},\)|\1 \"COPYING.LIB\"${FREEZE}, |" \
	%{gem_name}.gemspec
# vte3 should be okay, pkgconfig(vte-2.91) not strictly needed.
# hacking
sed -i dependency-check/Rakefile \
	-e '\@PKGConfig\.check_version@s|vte-2.91|glib-2.0|'
sed -i -e '\@s\.extensions@d'  %{gem_name}.gemspec

%build
export CONFIGURE_ARGS="--with-cflags='%{optflags} -Werror-implicit-function-declaration'"
export CONFIGURE_ARGS="$CONFIGURE_ARGS --with-pkg-config-dir=$(pwd)%{_libdir}/pkgconfig"
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/


pushd %{buildroot}
rm -f .%{gem_extdir_mri}/{gem_make.out,mkmf.log}
popd
pushd %{buildroot}%{gem_instdir}
rm -rf \
	dependency-check/ \
	%{nil}
popd

# Cleanups
pushd %{buildroot}
rm -rf \
	.%{gem_instdir}/Rakefile \
	.%{gem_instdir}/extconf.rb \
	.%{gem_instdir}/ext/
popd

%check
pushd .%{gem_instdir}
sed -i test/run-test.rb \
	-e '\@exit Test::Unit::AutoRunner@s|,[ \t]*File\.join(.*"test")||'

RANDR_OPTS=""
%if 0%{?fedora} >= 25
RANDR_OPTS="-extension RANDR"
%endif

xvfb-run -s "-screen 0 640x480x24 $RANDR_OPTS" \
	ruby -Ilib:tmp:test ./test/run-test.rb
popd

%files
%dir	%{gem_instdir}/
%license	%{gem_instdir}/[A-Z]*
%exclude	%{gem_instdir}/Rakefile
%dir	%{gem_instdir}/lib/
%{gem_instdir}/lib/%{gem_name}.rb
%dir	%{gem_instdir}/lib/%{gem_name}/
%{gem_instdir}/lib/%{gem_name}/*.rb

%exclude %{gem_cache}
%exclude	%{gem_instdir}/*gemspec
%{gem_spec}

%files	doc
%doc	%{gem_docdir}/
%exclude	%{gem_instdir}/test

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec  6 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.1-1
- 3.4.1

* Tue Oct 15 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.0-1
- 3.4.0

* Sun Sep  8 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.7-1
- 3.3.7

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.6-1
- 3.3.6

* Mon Feb 18 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.2-1
- 3.3.2

* Sat Feb  2 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.1-1
- 3.3.1

* Sun Nov 18 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.0-1
- 3.3.0

* Mon Aug 13 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.9-1
- 3.2.9

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.7-1
- 3.2.7

* Thu May  3 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.5-1
- 3.2.5

* Fri Apr 20 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.4-1
- 3.2.4

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 29 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.1-1
- 3.2.1
- Use vte291 for F-28

* Wed Nov 15 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.0-1
- 3.2.0

* Tue Oct 24 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.9-1
- 3.1.9

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.8-1
- 3.1.8

* Fri Jul 14 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.7-1
- 3.1.7

* Thu Jun  8 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.6-1
- 3.1.6

* Fri May  5 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.3-1
- 3.1.3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.1-1
- 3.1.1

* Wed Nov 30 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.0-1
- 3.1.0

* Mon Aug 15 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.9-1
- 3.0.9

* Tue Apr 19 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.8-1
- 3.0.8

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Oct 11 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.7-1
- 3.0.7

* Wed Sep 23 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.5-2
- Patches from the upstream git

* Wed Sep 23 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.5-1
- 3.0.5

* Tue Sep 22 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.4-1
- 3.0.4

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 29 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.5-1
- 2.2.5

* Fri Jan 16 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.4-3
- F-22: Rebuild for ruby 2.2

* Fri Jan 02 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.4-2
- Some cleanups

* Tue Dec 30 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.4-1
- Initial package
