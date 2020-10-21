Summary: Java bindings for BLAS
Name: jblas
Version: 1.2.4
Release: 13%{?dist}
License: BSD
URL: http://jblas.org

Source0: https://github.com/mikiobraun/jblas/archive/jblas-%{version}.tar.gz
Patch0: 0001-Try-to-load-libraries-directly-on-Linux.patch
Patch1: 0002-build.xml-fix-version.patch
# workaround for build failure on ppc64
# than, still investigate why libsyms returns empty array on ppc64
Patch2: jblas-1.2.3-ppc64.patch
Patch3: 0002-Prevent-resource-leak-by-closing-resources-in-load-s.patch
# https://github.com/mikiobraun/jblas/pull/85
Patch4: 0003-javadoc-use-html-entities-unicode-and-fix-formatting.patch
Patch5: 0004-javadoc-add-summaries-to-tables.patch
Patch6: 0005-Fix-path-to-stylesheet-and-overview.patch

BuildRequires:  javapackages-local
BuildRequires:  ant
BuildRequires:  ruby-devel
BuildRequires:  gcc-gfortran
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)

BuildRequires:  junit
BuildRequires:  atlas-devel

BuildRequires:  rubygem-RedCloth
BuildRequires:  rubygem-hitimes
BuildRequires:  rubygem-nokogiri
BuildRequires:  rubygem-redcarpet
BuildRequires:  rubygem-ffi
BuildRequires:  rubygem-posix-spawn
BuildRequires:  rubygem-fog-json
# fast-stemmer

%description
Wraps BLAS (e.g. ATLAS) using generated code through JNI. Allows Java
programs to use the full power of ATLAS/Lapack through a convenient
interface.

Uninstalling generic atlas rpm and installing an architecture-specific
version of atlas (e.g. atlas-sse3) is recommended.

%package javadoc
Summary:        Javadocs for %{name}
Requires:       jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -qn %{name}-%{name}-%{version}
rm -rf src/main/resources/lib/static
%patch0 -p1
%patch1 -p1
%ifarch ppc64
%patch2 -p1
%endif
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

# turn of javadoc warnings, we don't care
sed -i.bak -r 's/overview=/additionalparam="-Xdoclint:none" \0/' build.xml

sed -i.bak -r 's/-SNAPSHOT//' build.xml

ln -s pom.xml %{name}.pom
%mvn_file org.jblas:jblas %{name}

%build
libdir="$(cd "/usr/lib/$(gcc -print-multi-os-directory)"; pwd)"
export LC_ALL=C.UTF-8
./configure --ptatlas --libpath="$libdir/atlas" --arch-flavor=sse --libs=tatlas
%make_build CFLAGS="%{optflags} -fPIC"
ant minimal-jar javadoc
rm -rf javadoc/src-html

ln -s jblas-minimal-%{version}*.jar %{name}.jar

%mvn_artifact %{name}.pom %{name}.jar

%install
%mvn_install -J javadoc

install -d -m 755 %buildroot%{_libdir}/%{name}
install -pm 755 src/main/resources/lib/dynamic/Linux/*/sse/libjblas.so \
                %buildroot%{_libdir}/%{name}/

%files -f .mfiles
%{_libdir}/%{name}
%license COPYING AUTHORS
%doc RELEASE_NOTES

%files javadoc -f .mfiles-javadoc

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-13
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.2.4-11
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.4-7
- Use C.UTF-8 locale
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug  7 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.4-4
- Replace deprecated %%add_maven_depmap with %%mvn_file/%%mvn_install

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 25 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.4-1
- Update to latest version
- Clean up spec file

* Tue Nov 15 2016 Than Ngo <than@redhat.com> - 1.2.3-11
- add BR on ruby-devel → fix build failure
- add workaround to fix build failure on ppc64

* Sun Nov 13 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.3-10
- Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.3-6
- Fix rawhide build (#1106829).

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Feb 22 2014 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.3-4
- Prune dependency on jpackage-utils and depend on java-headless (#1068201).

* Sun Sep 22 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.3-3
- Bump release for rebuild after libatlas so name bump.

* Mon Aug 05 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.3-2
- Make /usr/lib64/jblas owned.

* Tue Jul 30 2013 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.3-1
- Initial packaging (#990627).
