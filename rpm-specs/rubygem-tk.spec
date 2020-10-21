%global	gem_name	tk

Name:		rubygem-%{gem_name}
Version:	0.3.0
Release:	1%{?dist}

Summary:	Tk interface module using tcltklib
License:	BSD or Ruby
URL:		https://github.com/ruby/tk
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:	gcc
BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	ruby-devel
BuildRequires:	tk-devel
Obsoletes:		ruby-tcltk < 2.4.0
# No provides for now

%description
Tk interface module using tcltklib.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
grep -rlZ /usr/local/bin . | \
	xargs -0 sed -i -e 's|/usr/local/bin|%{_bindir}|g'
grep -rlZ /usr/bin/env . | \
	xargs -0 sed -i -e 's|/usr/bin/env ruby|%{_bindir}/ruby|'
find . -name \*.rb -print0 | xargs -0 grep -lZ '^#![ \t]*%{_bindir}' | \
	xargs -0 sed -i -e '\@^#![ \t]*%{_bindir}@d'
find . -name \*.rb -print0 | xargs -0 chmod 0644
find sample -type f -print0 | xargs -0 grep -lZ '^#![ \t]*%{_bindir}' | \
	xargs -0 chmod 0755

gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/* \
	%{buildroot}%{gem_extdir_mri}/

rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
	.gitignore \
	.travis.yml \
	Gemfile \
	README.macosx-aqua \
	README.tcltklib \
	Rakefile \
	old-README.tcltklib.ja \
	%{gem_name}.gemspec \
	bin/ \
	ext/ \
	%{nil}
popd
pushd %{buildroot}%{gem_extdir_mri}
# Just to shut up rpmlint
# For gem, it is sufficient that gem.build_complete file
# "exists" (gem checks the existence of gem.build_complete file),
# however rpmlint complains if the file is null-size
# Not using the following hack fornow
#test -f gem.build_complete && echo "complete" > gem.build_complete
rm -f \
	mkmf.log \
	gem_make.out \
	%{nil}
popd

%check
# No check currently

%files
%dir %{gem_instdir}
%license	%{gem_instdir}/BSDL
%license	%{gem_instdir}/LICENSE.txt
%doc	%{gem_instdir}/README.1st
%doc	%{gem_instdir}/README.md

%{gem_libdir}/

%{gem_extdir_mri}/
%{gem_spec}

%files doc
%doc	%{gem_docdir}
%doc	%{gem_instdir}/README.fork
%{gem_instdir}/sample

%doc	%{gem_instdir}/README.ActiveTcl
%doc	%{gem_instdir}/MANUAL_tcltklib.eng
%doc	%{gem_instdir}/MANUAL_tcltklib.ja

%changelog
* Fri Oct  9 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.0-1
- 0.3.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.0-9
- F-32: rebuild against ruby27

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.0-6
- F-30: rebuild against ruby26

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.2.0-3
- Rebuilt for switch to libxcrypt

* Wed Jan 03 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.0-2
- F-28: rebuild for ruby25

* Fri Aug  4 2017 Mamoru TASAKA <mtasaka@tbz.t-com.ne.jp> - 0.2.0-1
- 0.2.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 27 2017 Mamoru TASAKA <mtasaka@tbz.t-com.ne.jp> - 0.1.2-2
- Reflect comments on review request

* Wed Mar 15 2017 Mamoru TASAKA <mtasaka@tbz.t-com.ne.jp> - 0.1.2-1
- 0.1.2

* Sun Jan  1 2017 Mamoru TASAKA <mtasaka@tbz.t-com.ne.jp> - 0.1.1-1
- Initial package
