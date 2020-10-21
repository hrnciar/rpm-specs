Name:           opencsg
Version:        1.4.2
Release:        12%{?dist}
Summary:        Library for Constructive Solid Geometry using OpenGL
# license.txt contains a linking exception for CGAL
License:        GPLv2 with exceptions
URL:            http://www.opencsg.org/
Source0:        http://www.opencsg.org/OpenCSG-%{version}.tar.gz
Patch0:         %{name}-build.patch
BuildRequires:  gcc-c++, qt-devel, freeglut-devel, glew-devel, dos2unix

%description
OpenCSG is a library that does image-based CSG rendering using OpenGL.

CSG is short for Constructive Solid Geometry and denotes an approach to model
complex 3D-shapes using simpler ones. I.e., two shapes can be combined by
taking the union of them, by intersecting them, or by subtracting one shape
of the other. The most basic shapes, which are not result of such a CSG
operation, are called primitives. Primitives must be solid, i.e., they must
have a clearly defined interior and exterior. By construction, a CSG shape is
also solid then.

Image-based CSG rendering (also z-buffer CSG rendering) is a term that denotes
algorithms for rendering CSG shapes without an explicit calculation of the
geometric boundary of a CSG shape. Such algorithms use frame-buffer settings
of the graphics hardware, e.g., the depth and stencil buffer, to compose CSG
shapes. OpenCSG implements a variety of those algorithms, namely the
Goldfeather algorithm and the SCS algorithm, both of them in several variants.

%package devel
Summary: OpenCSG development files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for OpenCSG.

%prep
%setup -q -n OpenCSG-%{version}
%patch0 -p1

rm src/Makefile RenderTexture/Makefile Makefile example/Makefile
dos2unix license.txt

# Encoding
iconv --from=ISO-8859-1 --to=UTF-8 changelog.txt > changelog.txt.new && \
touch -r changelog.txt changelog.txt.new && \
mv changelog.txt.new changelog.txt

# New FSF Address
for FILE in src/*.h src/*.cpp include/opencsg.h
do
  sed -i s/"59 Temple Place, Suite 330, Boston, MA 02111-1307 USA"/"51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA"/ $FILE
done

# Use Fedora's glew
rm -rf glew/

%build
%{qmake_qt4}
make %{?_smp_mflags}

%install
# No make install
chmod g-w lib/*
mkdir -p %{buildroot}/%{_libdir}
mkdir -p %{buildroot}/%{_includedir}
cp -pP lib/* %{buildroot}/%{_libdir}/
cp -p include/opencsg.h %{buildroot}/%{_includedir}/

%files
%doc changelog.txt doc license.txt
%{_libdir}/*so.*

%files devel
%{_includedir}/*
%{_libdir}/*so

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.4.2-8
- Rebuilt for glew 2.1.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 1.4.2-2
- Rebuild for glew 2.0.0

* Thu Sep 29 2016 Miro Hrončok <mhroncok@redhat.com> - 1.4.2-1
- New version 1.4.2 (#1380373)

* Thu Sep 15 2016 Miro Hrončok <mhroncok@redhat.com> - 1.4.1-1
- New version 1.4.1 (#1376267)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Rex Dieter <rdieter@fedoraproject.org> 1.4.0-5
- use %%qmake_qt4 macro

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 1.4.0-4
- Rebuild for glew 1.13

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.4.0-2
- Rebuilt for GCC 5 C++11 ABI change

* Fri Sep 19 2014 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-1
- New version 1.4.0 (#1142964)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Miro Hrončok <mhroncok@redhat.com> - 1.3.3-1
- Updated to 1.3.3

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 1.3.2-11
- rebuilt for GLEW 1.10

* Sun Nov 17 2013 Miro Hrončok <mhroncok@redhat.com> - 1.3.2-10
- Rebuilt for new glew

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 13 2012 Adam Jackson <ajax@redhat.com> - 1.3.2-7
- Rebuild for glew 1.9.0

* Wed Nov 14 2012 Miro Hrončok <miro@hroncok.cz> - 1.3.2-6
- Removed FSF Address path
   - using sed instead, so the path is not needed to update in newer version
   - don't modify license file
- License exception explained in a comment
- Dropped doc form devel package
- Usiyng cp -pP instead of mv to preserve timestamps

* Mon Oct 8 2012 Miro Hrončok <miro@hroncok.cz> - 1.3.2-5
- Added img to doc (needed by html files)
- Added odc to devel package (to avoid W: no-documentation)

* Thu Jul 5 2012 Greg Jurman <gdj2214@rit.edu> - 1.3.2-4
- Removed extranous build-depend to libXmu
- Fix undefined-non-weak-symbol for libGLEW
- Deprecate patch for fixing build order now the example program is gone
- Remove dependencies to qtGui and qtCore
- Remove example application from package
- Fix newlines in license.txt

* Thu Jun 7 2012 Greg Jurman <gdj2214@rit.edu> - 1.3.2-3
- Fixed spec according to Volker's suggestions

* Wed May 30 2012 Greg Jurman <gdj2214@rit.edu> - 1.3.2-2
- Fixed incorrect-fsf-address lint error

* Sat May 26 2012 Greg Jurman <gdj2214@rit.edu> - 1.3.2-1
- Updated source material for OpenCSG version 1.3.2
- Patched opencsg.pro to build in proper order (src then example)
- Patched example.pro to require libGLU (else error is thrown)
- Fixed devel/debuginfo cpio call 'missing include/opencsg.h'

* Sat Mar  5 2011 Jeff Moe <moe@alephobjects.com> - 1.3.1-5
- Enable parallel compiling.
- Corrected license to GPLv2 with exceptions.
- Improved -devel Requires for multilib.
- Remove BuildRoot tag.
- Remove %%clean section
- Change mv and mkdir to direct commands, not macros.

* Sat Feb 26 2011 Jeff Moe <moe@alephobjects.com> - 1.3.1-4
- Regenerate Makefiles to fix rpath and debuginfo-without-sources
- Use Fedora's glew instead of included copy
- Remove tab from .spec

* Mon Feb 21 2011 Jeff Moe <moe@alephobjects.com> - 1.3.1-3
- Add ldconfig to %%post and %%postun
- Fix rpath
- Fix library permissions

* Sun Feb 20 2011 Jeff Moe <moe@alephobjects.com> - 1.3.1-2
- Use qmake macro

* Sun Feb 20 2011 Jeff Moe <moe@alephobjects.com> - 1.3.1-1
- Add -devel package
- Add BuildRequires

* Fri Feb 18 2011 Jeff Moe <moe@alephobjects.com> - 1.3.1-0
- Initial spec

