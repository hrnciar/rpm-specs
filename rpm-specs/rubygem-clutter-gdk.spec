%global	gem_name	clutter-gdk

%undefine        _changelog_trimtime

Name:		rubygem-%{gem_name}
Version:	3.4.3
Release:	1%{?dist}

Summary:	Ruby binding of GDK specific API of Clutter
License:	LGPLv2+
URL:		http://ruby-gnome2.osdn.jp/

Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
# pull in additional files from the upstream
#Source1:	https://raw.githubusercontent.com/ruby-gnome2/ruby-gnome2/master/clutter-gdk/COPYING.LIB
#Source2:	https://raw.githubusercontent.com/ruby-gnome2/ruby-gnome2/master/clutter-gdk/README.md

BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
# No tests currently
#BuildRequires:	rubygem(clutter)
#BuildRequires:	rubygem(gdk3)
#BuildRequires:	clutter-gtk
Requires:		clutter-gtk

BuildArch:		noarch

%description
Ruby/ClutterGDK is a Ruby binding of GDK specific API of Clutter.


%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:		noarch

%description	doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

# Allow ruby-gnome2 no less than ones
sed -i -e 's|= 3\.4\.3|>= 3.4.3|' %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -f \
	Rakefile \
	%{nil}
popd

%check
# No check currently

%files
%dir	%{gem_instdir}
# Gem usually places license file below %%gem_instdir
%license	%{gem_instdir}/COPYING.LIB
%doc	%{gem_instdir}/README.md
%exclude	%{gem_instdir}/Rakefile

%{gem_libdir}
%exclude	%{gem_instdir}/*gemspec
%{gem_spec}

%files doc
%doc	%{gem_docdir}

%changelog
* Thu Aug 13 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.3-1
- 3.4.3

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec  4 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.1-1
- 3.4.1

* Mon Oct 14 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.0-1
- 3.4.0

* Sun Sep  8 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.7-1
- 3.3.7

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 18 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.6-1
- 3.3.6

* Mon Feb 18 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.2-1
- 3.3.2

* Fri Feb  1 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.1-1
- 3.3.1

* Fri Nov 16 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.0-1
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

* Tue Nov 14 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.0-1
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

* Sat Dec 31 2016 Mamoru TASAKA <mtasaka@fedoraprojec.org> - 3.1.0-1
- Initial package
