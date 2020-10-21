%global	gem_name	opengl

%global	bootstrap	1

# examples/OrangeBook/: BSD
# examples/NeHe: KILLED (license unclear)
# examples/RedBook/ SGI = MIT
# examples/misc/OGLBench.rb: GPL+ or Artistic
# examples/misc/fbo_test.rb ??? KILLED
# examples/misc/trislam.rb: GPL+ or Artistic

Name:		rubygem-%{gem_name}
Version:	0.10.0
Release:	14%{?dist}

Summary:	An OpenGL wrapper for Ruby
License:	MIT
URL:		https://github.com/drbrain/opengl
# Source0:	https://rubygems.org/gems/%%{gem_name}-%%{version}.gem
# The above gem file contains files with unclear license,
# we use a regenerated gem as a Source0 with such files
# removed.
# Source0 is generated using Source1.  
Source0:	%{gem_name}-%{version}-clean.gem
Source1:	create-clean-opengl-gem.sh
# http://www.gnu.org/licenses/old-licenses/gpl-1.0.txt
Source2:	GPLv1.rubygem_opengl

# MRI (CRuby) only
BuildRequires:	gcc
BuildRequires:	ruby-devel
BuildRequires:	rubygems-devel
BuildRequires:	libGL-devel
BuildRequires:	libGLU-devel
BuildRequires:	freeglut-devel
# %%check
%if 0%{?bootstrap} < 1
BuildRequires:	rubygem(minitest) >= 5
BuildRequires:	%{_bindir}/xvfb-run
BuildRequires:	mesa-dri-drivers
BuildRequires:	rubygem(glu)
BuildRequires:	rubygem(glut)
%endif
%if 0%{?fedora} <= 21
# Install this for compatibility
Requires:	rubygem(glu)
Requires:	rubygem(glut)
%endif


%description
An OpenGL wrapper for Ruby. ruby-opengl contains bindings for OpenGL and the
GLU and GLUT libraries.


%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
License:	MIT and BSD and (GPL+ or Artistic)
BuildArch:	noarch

%description	doc
Documentation for %{name}

%prep
%setup -q -c -T

# Gem repack
TOPDIR=$(pwd)
mkdir tmpunpackdir
pushd tmpunpackdir

gem unpack %{SOURCE0}
cd %{gem_name}-%{version}-clean
gem specification -l --ruby %{SOURCE0} > %{gem_name}.gemspec

find examples/ -type f -print0 | xargs --null file | \
	grep CRLF | sed -e 's|:.*$||' | \
	while read f
do
	sed -i -e 's|\r||' $f
done

sed -i.minitest \
	-e 's|MiniTest::Unit::TestCase|Minitest::Test|' \
	lib/opengl/test_case.rb

gem build %{gem_name}.gemspec
mv %{gem_name}-%{version}.gem $TOPDIR

popd
rm -rf tmpunpackdir

%build
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}/
cp -pa .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

install -cpm 644 %{SOURCE2} \
	%{buildroot}%{gem_instdir}/examples/misc/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a ./%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/

pushd %{buildroot}
rm -f .%{gem_extdir_mri}/{gem_make.out,mkmf.log}
popd

# cleanups
pushd %{buildroot}%{gem_instdir}
rm -rf \
	.autotest .gemtest .gitignore .travis.yml \
	Gemfile \
	Manifest.txt \
	Rakefile* \
	*gemspec \
	docs/build_install.txt \
	ext/ \
	test/

find examples/ utils/ -type f -perm /100 \
	-exec chmod ugo-x {} \;

popd

rm -f %{buildroot}%{gem_extdir_mri}/lib/opengl/test_case.rb

%check
%if 0%{?bootstrap} < 1
pushd .%{gem_instdir}

cat > test/unit.rb << EOF
gem "minitest"
require "minitest/autorun"
EOF

xvfb-run \
	-s "-screen 0 640x480x24" \
	ruby \
		-Ilib:.:./ext \
		-e "Dir.glob('test/test_*.rb').each { |f| require f }" \
		|| echo "please check this later"
popd
%endif

%files
%dir	%{gem_instdir}
%license	%{gem_instdir}/MIT-LICENSE
%doc	%{gem_instdir}/History.md
%doc	%{gem_instdir}/README.rdoc

%{gem_libdir}/
%{gem_extdir_mri}/

%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc	%{gem_docdir}
%doc	%{gem_instdir}/examples/
%doc	%{gem_instdir}/utils/

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.0-12
- F-32: rebuild against ruby27

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.0-9
- F-30: rebuild against ruby26
- Once disable tests for bootstrap

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.10.0-6
- Rebuilt for switch to libxcrypt

* Thu Jan 04 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.0-5
- Enable tests again

* Thu Jan 04 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.0-4
- F-28: rebuild for ruby25
- Once disable tests for bootstrap

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.0-1
- Enable tests

* Fri Jun 30 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.10.0-0.1
- 0.10.0
- Once disable tests

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 11 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.2-10
- Enable test again

* Wed Jan 11 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.2-9
- F-26: rebuild for ruby24
- Once disable test for bootstrap

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.2-7
- F-24: rebuild against ruby23

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 16 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.2-5
- Enable test again

* Fri Jan 16 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.2-4
- F-22: Rebuild for ruby 2.2
- Bootstrap, once disable test

* Sun Jan 11 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.2-3
- Enable test

* Sun Jan 11 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.2-1
- 0.9.2
- bootstrap, once disabling test

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May  3 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.2-4
- F-21: rebuild for ruby 2.1 / rubygems 2.2

* Wed Oct 30 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.0-2
- Misc fixes with review (bug 1024168)

* Tue Oct 29 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.0-1
- Initial package
