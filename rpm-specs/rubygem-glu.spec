%global	gem_name	glu

%global	need_bootstrap	0

Name:		rubygem-%{gem_name}
Version:	8.3.0
Release:	14%{?dist}

Summary:	Glu bindings for the opengl gem
License:	MIT
URL:		https://github.com/larskanis/glu
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:	gcc
BuildRequires:	rubygems-devel 
BuildRequires:	ruby-devel
BuildRequires:	libGL-devel
BuildRequires:	libGLU-devel
# %%check
%if 0%{?need_bootstrap} < 1
BuildRequires:	rubygem(minitest) >= 5
BuildRequires:	rubygem(opengl)
BuildRequires:	%{_bindir}/xvfb-run
BuildRequires:	mesa-dri-drivers
BuildRequires:	rubygem(opengl) >= 0.9
BuildRequires:	rubygem(glut)
%endif

%description
Glu bindings for the opengl gem.

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
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/

pushd %{buildroot}
rm -f .%{gem_extdir_mri}/{gem_make.out,mkmf.log}
popd


pushd %{buildroot}%{gem_instdir}
rm -rf \
	.autotest .gemtest .gitignore .travis.yml \
	Rakefile \
	ext/ \
	test/
popd

%check
%if 0%{?need_bootstrap} < 1
pushd .%{gem_instdir}

%ifarch %arm
exit 0
%endif

xvfb-run \
	-s "-screen 0 640x480x24" \
	ruby \
		-Ilib:.:./ext \
		-e "Dir.glob('test/test_*.rb').each { |f| require f }"
popd
%endif

%files
%dir	%{gem_instdir}
%license	%{gem_instdir}/MIT-LICENSE
%doc	%{gem_instdir}/History.rdoc
%doc	%{gem_instdir}/Manifest.txt
%doc	%{gem_instdir}/README.rdoc

%{gem_libdir}/
%{gem_extdir_mri}/

%exclude	%{gem_cache}
%{gem_spec}

%files doc
%doc	%{gem_docdir}

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.0-13
- Enable tests again

* Fri Jan 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.0-12
- F-32: rebuild against ruby27
- Once disable tests for bootstrap

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.0-9
- F-30: rebuild against ruby26
- Once disable tests for bootstrap

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 8.3.0-6
- Rebuilt for switch to libxcrypt

* Thu Jan 04 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.0-5
- F-28: rebuild for ruby25

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.3.0-1
- 8.3.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 11 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.2-4
- Enable test again

* Wed Jan 11 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.2-3
- F-26: rebuild for ruby24
- Once disable test for bootstrap

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.2-1
- 8.2.2

* Wed Jan 13 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.1-7
- F-24: rebuild against ruby23
- Bootstrap, once disable test

* Tue Jul  7 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.1-6
- Disable test on arm for now

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 16 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.1-4
- Enable test again

* Fri Jan 16 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.1-3
- F-22: Rebuild for ruby 2.2
- Bootstrap, once disable test

* Sun Jan 11 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.1-2
- Enable test

* Thu Dec 18 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 8.2.1-1
- Initial package
