%define libname %mklibname txc-dxtn
%define develname %mklibname -d txc-dxtn

Name:		libtxc_dxtn
Summary:	S3 Texture Compression (S3TC) sextension for Mesa
Version:	1.0.1
Epoch:		1
Release:	SINCE MESA 17.3.0 THIS PACKAGE IS NOT NEEDED
Group:		System/Libraries
License:	BSD
URL:		https://cgit.freedesktop.org/~mareko/libtxc_dxtn/
Source0:	http://cgit.freedesktop.org/~mareko/libtxc_dxtn/snapshot/libtxc_dxtn-%{version}.tar.bz2
BuildRequires:	pkgconfig(gl)

%description
An open source implementation of the S3 Texture Compression (S3TC)
for use with the open source OpenGL implementation Mesa.

This provides the GLX extension GL_EXT_texture_compression_s3tc.

This package is in restricted because S3TC is covered by software
patents.

#-----------------------------------------------------------

%package -n %{develname}
Summary:	S3 Texture Compression (S3TC) sextension for Mesa
Group:		System/Libraries
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{develname}
An open source implementation of the S3 Texture Compression (S3TC)
for use with the open source OpenGL implementation Mesa.

This provides the GLX extension GL_EXT_texture_compression_s3tc.

This package is in restricted because S3TC is covered by software
patents.

%package -n %{libname}
Summary:	S3 Texture Compression (S3TC) sextension for Mesa
Group:		System/Libraries

%description -n %{libname}
An open source implementation of the  S3 Texture Compression (S3TC)
for use with the open source OpenGL implementation Mesa.

This provides the GLX extension GL_EXT_texture_compression_s3tc.

This package is in restricted because S3TC is covered by software
patents.

#-----------------------------------------------------------

%prep
%setup -q

%build
[[ -f configure ]] || ./autogen.sh
%setup_compile_flags
%configure
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/%{name}.so

%files -n %{develname}
%doc Changelog
%{_includedir}/txc_dxtn.h

